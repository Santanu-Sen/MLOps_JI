from gtts import gTTS
import pygame
import time
import os
from zenml import step


@step
def text_to_speech(text: str, language: str):
    # Convert text to speech
    speech = gTTS(text=text, lang=language, slow=False)

    #Save the speech to a temporary file
    speech_file = os.path.join(os.getcwd(), "temp.mp3")
    speech.save(speech_file)
    pygame.mixer.init()
    pygame.mixer.music.load(speech_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    
    # # Remove the temporary file
    pygame.mixer.music.stop()

    # # # Retry deletion with a delay
    # os.remove(speech_file)

