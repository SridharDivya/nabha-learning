"""AI assistant for students and teachers.

Real AI answers use ONE of these providers (checked in this order):
    GEMINI_API_KEY     free key from Google AI Studio (free tier, no card needed)
    ANTHROPIC_API_KEY  paid Anthropic API key
If neither is set (or the call fails), the assistant falls back to searching the
lesson content stored in the app, so the page always gives a useful answer.

Optional environment variables:
    GEMINI_MODEL       Gemini model name (default: gemini-3.8-flash)
    AI_MODEL           Anthropic model name (default: claude-sonnet-5-5)
"""
import math
import os
import re
import time
import requests

API_URL = 'https://api.anthropic.com/v1/messages'
GEMINI_URL = 'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent'
DEFAULT_GEMINI_MODEL = 'gemini-3.8-flash'
DEFAULT_MODEL = 'claude-sonnet-5-5'
MAX_HISTORY = 10
MAX_MESSAGE_CHARS = 1000


def build_system_prompt(role, grade, subject_titles):
    subjects = ', '.join(subject_titles) if subject_titles else 'the school syllabus'
    if role == 'teacher':
        return (
            "You are an AI assistant for school teachers at a digital learning platform for rural "
            "schools in Nabha, Punjab, India (Classes 5 to 10, NCERT/PSEB style syllabus). "
            "Help with lesson plans, simple explanations, classroom activities that need little equipment, "
            "quiz questions with answers, worksheets, and ideas for students who are struggling. "
            "Keep answers practical and concise. When asked for quiz questions, give 4 options (A-D) and mark the correct one. "
            "Reply in the language the teacher writes in."
        )
    return (
        f"You are a friendly AI tutor for a Class {grade} student at a rural school in Nabha, Punjab, India. "
        f"Their subjects are: {subjects}. "
        "Explain ideas in simple words, step by step, with small everyday examples (farms, village life, markets). "
        "Keep answers short (under 150 words unless asked for more). "
        "If the student asks for homework or quiz answers, guide them with hints and explain the method instead of only giving the final answer. "
        "Stay on school learning topics and be encouraging. "
        "Reply in the language the student writes in (English, Hindi, Punjabi or Telugu)."
    )


def _clean_history(history):
    cleaned = []
    for item in (history or [])[-MAX_HISTORY:]:
        role = item.get('role')
        text = str(item.get('content', ''))[:MAX_MESSAGE_CHARS].strip()
        if role in ('user', 'assistant') and text:
            cleaned.append({'role': role, 'content': text})
    # The API needs the conversation to start with a user message and alternate.
    while cleaned and cleaned[0]['role'] != 'user':
        cleaned.pop(0)
    merged = []
    for msg in cleaned:
        if merged and merged[-1]['role'] == msg['role']:
            merged[-1]['content'] += '\n' + msg['content']
        else:
            merged.append(msg)
    return merged


def ai_enabled():
    return bool(os.environ.get('GEMINI_API_KEY') or os.environ.get('ANTHROPIC_API_KEY'))


RETRY_STATUSES = {429, 500, 502, 503, 504}   # temporary Google-side problems worth retrying
MODELS_URL = 'https://generativelanguage.googleapis.com/v1beta/models?pageSize=100'
_model_cache = {'at': 0, 'models': []}


def _fallback_models(key, skip):
    """Ask Google which text models this key can use, and return a few 'flash' ones to try when the
    main model is busy. Cached for an hour. Lighter ('lite') models come first: they are the least busy."""
    if time.time() - _model_cache['at'] > 3600:
        names = []
        try:
            r = requests.get(MODELS_URL, headers={'x-goog-api-key': key}, timeout=8)
            if r.status_code == 200:
                for m in r.json().get('models', []):
                    name = m.get('name', '').replace('models/', '')
                    if ('generateContent' in m.get('supportedGenerationMethods', []) and 'flash' in name
                            and not any(x in name for x in ('image', 'tts', 'live', 'audio', 'embed', 'robotics'))):
                        names.append(name)
                names.sort(key=lambda n: ('lite' not in n, n), reverse=False)
                print(f'[ai_assistant] fallback models available: {names[:6]}', flush=True)
            else:
                print(f'[ai_assistant] could not list models: {r.status_code}', flush=True)
        except Exception as exc:
            print(f'[ai_assistant] could not list models: {exc!r}', flush=True)
        _model_cache.update(at=time.time(), models=names)
    return [n for n in _model_cache['models'] if n != skip][:2]


def _try_gemini_model(model, key, payload, attempts):
    """Returns (text_or_None, give_up_on_this_model_only)."""
    for attempt in range(attempts):
        try:
            response = requests.post(
                GEMINI_URL.format(model=model),
                headers={'x-goog-api-key': key, 'content-type': 'application/json'},
                json=payload, timeout=15)
            if response.status_code == 200:
                parts = response.json()['candidates'][0]['content']['parts']
                text = ''.join(p.get('text', '') for p in parts).strip()
                return text or None
            # Shows up in Render's Logs tab so a wrong key or model name is easy to spot.
            print(f'[ai_assistant] Gemini {model} error {response.status_code} (try {attempt + 1}/{attempts}): {response.text[:300]}', flush=True)
            if response.status_code not in RETRY_STATUSES:
                return None
        except Exception as exc:
            print(f'[ai_assistant] Gemini {model} call failed (try {attempt + 1}/{attempts}): {exc!r}', flush=True)
        if attempt < attempts - 1:
            time.sleep(2)
    return None


def _call_gemini(system_prompt, messages):
    key = os.environ.get('GEMINI_API_KEY')
    if not key:
        return None
    model = os.environ.get('GEMINI_MODEL', DEFAULT_GEMINI_MODEL)
    payload = {
        'system_instruction': {'parts': [{'text': system_prompt}]},
        'contents': [
            {'role': 'user' if m['role'] == 'user' else 'model', 'parts': [{'text': m['content']}]}
            for m in messages
        ],
        'generationConfig': {'maxOutputTokens': 900, 'temperature': 0.6},
    }
    text = _try_gemini_model(model, key, payload, attempts=2)
    if text:
        return text
    # Main model busy or unavailable: try other models this key can use (worst case ~65s, under gunicorn's 90s).
    for other in _fallback_models(key, skip=model):
        text = _try_gemini_model(other, key, payload, attempts=1)
        if text:
            print(f'[ai_assistant] answered using fallback model {other}', flush=True)
            return text
    return None


def _call_claude(system_prompt, messages):
    key = os.environ.get('ANTHROPIC_API_KEY')
    if not key:
        return None
    try:
        response = requests.post(
            API_URL,
            headers={
                'x-api-key': key,
                'anthropic-version': '2023-06-01',
                'content-type': 'application/json',
            },
            json={
                'model': os.environ.get('AI_MODEL', DEFAULT_MODEL),
                'max_tokens': 800,
                'system': system_prompt,
                'messages': messages,
            },
            timeout=20,
        )
        response.raise_for_status()
        blocks = response.json().get('content', [])
        text = ''.join(b.get('text', '') for b in blocks if b.get('type') == 'text').strip()
        return text or None
    except Exception:
        return None


STOPWORDS = {
    'the', 'and', 'for', 'are', 'was', 'were', 'what', 'whats', 'whts', 'how', 'why', 'who', 'when',
    'where', 'which', 'this', 'that', 'with', 'from', 'about', 'can', 'you', 'your', 'does', 'did',
    'tell', 'give', 'please', 'explain', 'help', 'let', 'have', 'has', 'not', 'any', 'all', 'our',
    'class', 'study', 'subject', 'subjects', 'topic', 'lesson', 'lessons', 'make', 'plan', 'plans',
    'easy', 'simple', 'activity', 'activities', 'question', 'questions', 'mcq', 'mcqs', 'quiz',
    'worksheet', 'teach', 'write', 'create', 'show', 'some', 'step',
}

# Requests that need a real AI to write something new (a fallback can only search lessons).
GENERATE_PATTERN = re.compile(
    r'\b(lesson plan|plan|mcqs?|quiz|worksheet|activity|activities|questions?|homework|essay|summary)\b')


def _stem(word):
    word = word.lower()
    return word[:-1] if len(word) > 3 and word.endswith('s') else word


def _lesson_search(question, units):
    """Offline fallback: rank lesson units by matching whole words, giving rare words more weight."""
    words = {_stem(w) for w in re.findall(r'[a-zA-Z]{3,}', question.lower()) if w not in STOPWORDS}
    if not words or not units:
        return None
    docs = []
    for unit in units:
        title_words = [_stem(w) for w in re.findall(r'[a-zA-Z]+', unit.title)]
        body_words = [_stem(w) for w in re.findall(r'[a-zA-Z]+', (unit.content or '') + ' ' + (unit.pdf_text or ''))]
        docs.append((unit, title_words, body_words))
    total = len(docs)
    scored = []
    weights = {}
    for w in words:
        df = sum(1 for _, t, b in docs if w in t or w in b)
        weights[w] = math.log((total + 1) / (df + 1)) + 0.1 if df else 0
    for unit, title_words, body_words in docs:
        score = sum(weights[w] * (min(body_words.count(w), 2) + (2 if w in title_words else 0)) for w in words)
        if score > 0:
            scored.append((score, unit))
    scored.sort(key=lambda pair: pair[0], reverse=True)
    if not scored:
        return None
    parts = []
    for _, unit in scored[:2]:
        excerpt = ((unit.content or '') + '\n' + (unit.pdf_text or '')).strip()
        if len(excerpt) > 600:
            excerpt = excerpt[:600].rsplit(' ', 1)[0] + '...'
        parts.append(f"{unit.subject.grade_level} {unit.subject.title} - {unit.title}\n{excerpt}")
    return '\n\n'.join(parts)


def ask_ai(role, grade, subject_titles, message, history, units):
    message = (message or '').strip()[:MAX_MESSAGE_CHARS]
    if not message:
        return {'reply': 'Please type a question.', 'source': 'none'}

    messages = _clean_history(history) + [{'role': 'user', 'content': message}]
    system_prompt = build_system_prompt(role, grade, subject_titles)
    reply = _call_gemini(system_prompt, messages) or _call_claude(system_prompt, messages)
    if reply:
        return {'reply': reply, 'source': 'ai'}

    asks_subjects = re.search(r'\b(subjects?|syllabus|study|studying)\b', message.lower())
    if asks_subjects and subject_titles and role == 'student':
        return {'reply': f"In Class {grade} you study: " + ', '.join(subject_titles) +
                         ". Ask me about any topic from these subjects!", 'source': 'lessons'}

    found = _lesson_search(message, units)
    busy = ai_enabled()      # a key is set, so the AI call itself failed (busy, quota, etc.)
    if GENERATE_PATTERN.search(message.lower()):
        if busy:
            reply = "The AI service is very busy right now. Please try again in a minute."
        else:
            reply = ("Writing lesson plans, quiz questions, worksheets or activities needs the AI service, "
                     "which is not switched on yet. Ask the site owner to add the AI key.")
        if found:
            reply += "\n\nMeanwhile, here is related lesson content already in your course:\n\n" + found
        return {'reply': reply, 'source': 'lessons' if found else 'none'}
    if found:
        note = ("(The AI service is busy right now, so here is the most relevant lesson content "
                "from your course. Try again in a minute for a full answer.)\n\n") if busy else \
               ("(The AI service is not switched on yet, so here is the most relevant lesson content "
                "from your course.)\n\n")
        return {'reply': note + found, 'source': 'lessons'}
    return {
        'reply': ("I couldn't find that in the lessons, and the AI service is busy right now. Please try again in a minute."
                  if busy else
                  "I couldn't find that in the lessons, and the AI service is not switched on yet. "
                  "Try different keywords, or ask your teacher to set up the AI key."),
        'source': 'none',
    }
