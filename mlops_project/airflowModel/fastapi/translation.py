from googletrans import Translator

def translate_text(text, target_language, source_language):
    # Translate the text to the target language
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language, src=source_language)

    return translated_text.text
