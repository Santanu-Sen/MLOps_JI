from googletrans import Translator
from zenml import step

@step
def translate_text(text: str, target_language: str, source_language: str) -> str:
    # Translate the text to the target language
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language, src=source_language)

    return translated_text.text
