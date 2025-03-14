from gpt4all import GPT4All
from speakListen import speak, hear
from voice_emotion import analyze_voice_emotion

# Load GPT4All Model
gpt_model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")

def chat_with_gpt4all(user_input):
    """Generates AI responses using GPT4All (local AI model)."""
    response = gpt_model.generate(user_input, max_tokens=50, temp=0.7)
    return response.strip()

def start_friend_mode():
    """Friend Mode - Free conversation + Emotion Analysis"""
    speak("You are now in Friend Mode. Let's talk!")

    while True:
        speak("How are you feeling?")
        emotion = analyze_voice_emotion()  # Analyze user's voice for emotion

        user_query = hear().lower()

        if "switch to assistant mode" in user_query:
            speak("Switching to Assistant Mode.")
            return  # Exit Friend Mode and return to `main.py`

        else:
            response = chat_with_gpt4all(user_query)
            print("Savin:", response)
            speak(response)
