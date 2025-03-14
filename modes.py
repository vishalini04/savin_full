import random
import pyttsx3

engine = pyttsx3.init()

roasts = [
    "You're like a software update. No one wants you, but we have to deal with you.",
    "Your code is like a horror movie—full of bugs and terrifying logic."
]

friend_responses = {
    "sad": [
        "It's okay to feel down sometimes. I'm here for you!",
        "Would you like me to play some calming music?"
    ],
    "joke": [
        "Why do Java developers wear glasses? Because they don’t C#."
    ]
}

personalities = {
    "shakespeare": "Ah, dear friend, thy worries shall vanish like morning mist!",
    "villain": "Mwahaha! You dare challenge me, mortal?"
}

def speak(text):
    engine.say(text)
    engine.runAndWait()

def handle_mode(mode, user_input):
    if mode == "roast":
        return random.choice(roasts)
    elif mode == "friend":
        if "sad" in user_input:
            return random.choice(friend_responses["sad"])
        elif "joke" in user_input:
            return random.choice(friend_responses["joke"])
    elif mode in personalities:
        return personalities[mode]
    else:
        return "I didn't understand that. Try again!"
