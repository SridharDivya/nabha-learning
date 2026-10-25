"""
Thin wrapper around an AI/machine translation backend so the rest of the app
doesn't need to know which translation library is in use.

Supported languages: English (en, default), Hindi (hi), Telugu (te).

If the translation service is unreachable (e.g. the school has no internet
that moment), functions here fail soft and return the original English text
instead of raising, so a lesson always still renders.
"""
from deep_translator import GoogleTranslator

SUPPORTED_LANGUAGES = {
    'en': 'English',
    'hi': 'हिन्दी (Hindi)',
    'te': 'తెలుగు (Telugu)',
}

# Language codes as understood by the browser's speech synthesis engine
# (used for voice narration), keyed the same way as SUPPORTED_LANGUAGES.
SPEECH_LANG_CODES = {
    'en': 'en-IN',
    'hi': 'hi-IN',
    'te': 'te-IN',
}

# deep-translator's chunk limit per request; long lesson text is split on
# sentence boundaries and translated in batches to stay under it.
_MAX_CHARS = 4500


def _translate_text(text, target_lang):
    if not text:
        return text
    if len(text) <= _MAX_CHARS:
        return GoogleTranslator(source='en', target=target_lang).translate(text)

    # Split long content into chunks so we don't exceed the request size limit.
    chunks, current = [], ''
    for sentence in text.split('. '):
        piece = sentence if sentence.endswith('.') else sentence + '. '
        if len(current) + len(piece) > _MAX_CHARS:
            chunks.append(current)
            current = piece
        else:
            current += piece
    if current:
        chunks.append(current)

    translator = GoogleTranslator(source='en', target=target_lang)
    return ''.join(translator.translate(chunk) for chunk in chunks)


def translate_lesson(title, content, target_lang):
    """
    Translates a lesson's title and content into target_lang.
    Returns (title, content) — untouched originals if target_lang is 'en',
    unsupported, or the translation service fails.
    """
    if target_lang not in SUPPORTED_LANGUAGES or target_lang == 'en':
        return title, content

    try:
        translated_title = _translate_text(title, target_lang)
        translated_content = _translate_text(content, target_lang) if content else content
        return translated_title, translated_content
    except Exception:
        # Offline, rate-limited, or the translation API is down — show English
        # rather than breaking the lesson page.
        return title, content
