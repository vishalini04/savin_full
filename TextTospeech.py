import pyttsx3
from gtts import gTTS
import os

def tts():
    """Converts text to speech."""
    audio = 'speech.mp3'
    language = 'en'
    sentence = input("Enter the text to be spoken: ")

    try:
        # Try using pyttsx3 (offline TTS)
        engine = pyttsx3.init()
        engine.say(sentence)
        engine.runAndWait()
    except Exception as e:
        print("Error with pyttsx3, switching to gTTS:", e)
        try:
            # Use gTTS as a backup (requires internet)
            tts = gTTS(text=sentence, lang=language, slow=False)
            tts.save(audio)
            os.system(f"start {audio}")  # For Windows
        except Exception as e:
            print("TTS failed completely:", e)

# Call the function for testing
# tts()
