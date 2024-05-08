from speech2text import speech_to_text
from text2speech import text_to_speech
from translation import translate_text




def main():


    print('Hello Folks!')
    
    # Choose source and target languages
    source_language = "en"  # English
    target_language = "hi"  # Hindi

    # Capture speech and convert it to text
    input_text = speech_to_text()

    if input_text:
        # Translate the text to the target language
        translated_text = translate_text(input_text, target_language, source_language)
        print('Translation is: ', translated_text)

        # Convert translated text to speech in the target language
        text_to_speech(translated_text, target_language)

    

if __name__ == "__main__":
    main()
