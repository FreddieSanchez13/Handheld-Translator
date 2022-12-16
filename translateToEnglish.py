from googletrans import Translator

def translate_to_english(text: str, source_language: str) -> str:
    translator = Translator()
    translation = translator.translate(text, src=source_language, dest='en')
    return translation.text