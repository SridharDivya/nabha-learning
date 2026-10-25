"""AI assistant for students and teachers.

If the ANTHROPIC_API_KEY environment variable is set, questions are answered by
Claude through the Anthropic API. If it is not set (or the call fails), the
assistant falls back to searching the lesson content stored in the app, so the
page always gives a useful answer.

Optional environment variables:
    ANTHROPIC_API_KEY  your API key (required for real AI answers)
    AI_MODEL           model name (default: claude-sonnet-5-5)
"""
import os
import re
import requests

API_URL = 'https://api.anthropic.com/v1/messages'
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
            timeout=40,
        )
        response.raise_for_status()
        blocks = response.json().get('content', [])
        text = ''.join(b.get('text', '') for b in blocks if b.get('type') == 'text').strip()
        return text or None
    except Exception:
        return None


def _lesson_search(question, units):
    """Offline fallback: find the lesson units that best match the question."""
    words = {w for w in re.findall(r'[a-zA-Z]{3,}', question.lower())}
    if not words:
        return None
    scored = []
    for unit in units:
        haystack = f"{unit.title} {unit.content or ''}".lower()
        score = sum(haystack.count(w) for w in words) + 3 * sum(w in unit.title.lower() for w in words)
        if score:
            scored.append((score, unit))
    scored.sort(key=lambda pair: pair[0], reverse=True)
    if not scored:
        return None
    parts = []
    for _, unit in scored[:2]:
        excerpt = (unit.content or '').strip()
        if len(excerpt) > 600:
            excerpt = excerpt[:600].rsplit(' ', 1)[0] + '...'
        parts.append(f"{unit.subject.grade_level} {unit.subject.title} - {unit.title}\n{excerpt}")
    return '\n\n'.join(parts)


def ask_ai(role, grade, subject_titles, message, history, units):
    message = (message or '').strip()[:MAX_MESSAGE_CHARS]
    if not message:
        return {'reply': 'Please type a question.', 'source': 'none'}

    messages = _clean_history(history) + [{'role': 'user', 'content': message}]
    reply = _call_claude(build_system_prompt(role, grade, subject_titles), messages)
    if reply:
        return {'reply': reply, 'source': 'ai'}

    found = _lesson_search(message, units)
    if found:
        note = ("(The AI service is not switched on yet, so here is the most relevant lesson content "
                "from your course.)\n\n")
        return {'reply': note + found, 'source': 'lessons'}
    return {
        'reply': "I couldn't find that in the lessons, and the AI service is not switched on yet. "
                 "Try different keywords, or ask your teacher to set up the AI key.",
        'source': 'none',
    }
