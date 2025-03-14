import sys
from speakListen import *
from websiteWork import *
from textRead import *
from dictator import *
from menu import *
from speechtotext import *
from TextTospeech import *
from openapps import *
from weather import *
import openai  # Import OpenAI
import os
from games import play_game
from reminder import set_reminder_voice, check_today_reminders, edit_reminder, delete_reminder
import sqlite3
from speakListen import speak, hear
from gpt4all import GPT4All
import datetime
from friend_mode import friend_mode  # ✅ Import the function, not the module
friend_mode()  # ✅ Now this correctly calls the function
import speech_recognition as sr

def assistant_mode():
    print("\n🔹 Assistant Mode Activated 🔹")
    speak("You are now in Assistant Mode. Give me commands!")

    while True:
        user_query = hear().lower()
        
        if "switch to friend mode" in user_query:
            speak("Switching to Friend Mode.")
            friend_mode()
            break  # Exit Assistant Mode when switching to Friend Mode
        elif "exit" in user_query:
            speak("Goodbye!")
            sys.exit()
        else:
            speak("I didn't understand. Please try again.")

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand that."
    except sr.RequestError:
        return "Speech recognition service is unavailable."
def process_command(command):
    if "friend mode" in command.lower():
        friend_mode()  
    elif "exit" in command.lower():
        print("Goodbye!")
        exit()
    else:
        print("Command not recognized.")

def main():
    print("\nSay \"Hello Buddy\" to activate the Voice Assistant!")
    speak("Hello! How can I assist you?")  # Updated greeting (removed weather announcement)

    while True:
        query = hear().lower()
        
        if not query or query == "none":
            speak("I couldn't hear you. Please try again.")
            continue

        if "weather" in query:
            speak("Which city's weather would you like to know?")
            city = hear().lower()
            weather_info = get_weather(city)
            speak(weather_info)
        elif "search" in query or "google" in query:
            speak("What do you want to search for?")
            search_query = hear().lower()
            google_search(search_query)
        elif "search youtube" in query or "youtube" in query:
            speak("What do you want to search for on YouTube?")
            search_query = hear().lower()
            search_youtube(search_query)  # ✅ Calls the function
        elif "send" in query and "whatsapp" in query:
            words = query.split()
            contact_index = words.index("to") + 1
            contact = words[contact_index]
            message = " ".join(words[words.index("send") + 1:contact_index - 1])
            send_whatsapp_message(contact, message)

        elif "play a game" in query or "start game" in query:
            play_game()

        elif "set a reminder" in query or "remind me" in query:
            set_reminder_voice()
        elif "what are my reminders" in query or "check reminders" in query:
            check_today_reminders()

        elif "write a note" in query or "type" in query:
            note_text = query.replace("write a note", "").replace("type", "").strip()
            write_in_notepad(note_text)
        elif "open" in query:
            app_name = query.replace("open", "").strip()
            open_app(app_name)
        elif "close" in query:
            app_name = query.replace("close", "").strip()
            close_app(app_name)
        elif "exit" in query or "quit" in query:
            speak("Goodbye!")
            sys.exit()
        else:
            speak("I'm not sure what you meant. Can you rephrase?")
        
        speak("What do you want me to do next?")  # Changed from closing after execution

main()
