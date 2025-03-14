import speech_recognition as sr
from speakListen import speak  # Importing speak function for feedback

# Initialize the recognizer
r = sr.Recognizer()

def stt():
    """Converts speech to text."""
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)  # Helps with background noise
        speak("I'm listening... Please speak now.")
        print("Listening...")

        try:
            audio_data = r.listen(source, timeout=10)  # Waits dynamically for speech
            print("Recognizing...")
            text = r.recognize_google(audio_data)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand. Please try again.")
            return "None"
        except sr.RequestError:
            speak("There was an error with the speech recognition service.")
            return "None"
        except Exception as e:
            speak(f"An error occurred: {e}")
            return "None"

# Call the function for testing
# stt()
