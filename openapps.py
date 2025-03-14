import os
from speakListen import speak
import webbrowser
import time
import pyautogui

def send_whatsapp_message(contact, message):
    """Sends a message on WhatsApp Web."""
    speak(f"Sending message to {contact} on WhatsApp.")
    whatsapp_url = f"https://web.whatsapp.com/send?phone={contact}&text={message.replace(' ', '%20')}"
    webbrowser.open(whatsapp_url)

def write_in_notepad(text):
    """Opens Notepad and types the given text."""
    speak("Opening Notepad and typing your note.")
    os.system("notepad")
    time.sleep(2)  # Wait for Notepad to open
    pyautogui.write(text, interval=0.1)

def open_app(app_name):
    """Opens applications based on user commands."""
    app_name = app_name.lower().strip()

    if "whatsapp" in app_name:
        speak("Opening WhatsApp...")
        os.system("start whatsapp")
    elif "instagram" in app_name:
        speak("Opening Instagram...")
        os.system("start chrome www.instagram.com")
    elif "facebook" in app_name:
        speak("Opening Facebook...")
        os.system("start chrome www.facebook.com")
    elif "discord" in app_name:
        speak("Opening Discord...")
        os.system("start discord")
    elif "notepad" in app_name:
        speak("Opening Notepad...")
        os.system("notepad")
    elif "calculator" in app_name:
        speak("Opening Calculator...")
        os.system("calc")
    elif "paint" in app_name:
        speak("Opening Paint...")
        os.system("mspaint")
    elif "youtube" in app_name:
        speak("Opening YouTube...")
        os.system("start chrome www.youtube.com")
    elif "spotify" in app_name:
        speak("Opening Spotify...")
        os.system("start spotify")
    elif "gmail" in app_name or "email" in app_name:
        speak("Opening Gmail...")
        os.system("start chrome mail.google.com")
    elif "file explorer" in app_name or "files" in app_name:
        speak("Opening File Explorer...")
        os.system("explorer")
    else:
        speak(f"Sorry, I couldn't find an application named {app_name}. Try specifying a valid app.")

def close_app(app_name):
    """Closes applications based on user commands."""
    app_name = app_name.lower().strip()

    # Define correct executable names
    app_processes = {
        "whatsapp": "WhatsApp.exe",
        "instagram": "chrome.exe",  # Closes Instagram tab in Chrome
        "facebook": "chrome.exe",  # Closes Facebook tab in Chrome
        "discord": "Discord.exe",
        "notepad": "notepad.exe",
        "calculator": "CalculatorApp.exe",
        "paint": "mspaint.exe",
        "spotify": "Spotify.exe",
        "file explorer": "explorer.exe"  # Fixed! Instead of force-closing, we restart it safely.
    }

    if app_name in app_processes:
        speak(f"Closing {app_name}...")
        process_name = app_processes[app_name]
        
        if app_name == "file explorer":
            os.system("taskkill /IM explorer.exe /F && start explorer")  # Restarts explorer safely
        else:
            os.system(f"taskkill /IM {process_name} /F")
    else:
        speak(f"Sorry, I couldn't find an application named {app_name} to close.")

def open_app_or_interact(query):
    """Determines whether to open an app or perform an action in it."""
    if "send" in query and "whatsapp" in query:
        words = query.split()
        contact_index = words.index("to") + 1
        contact = words[contact_index]
        message = " ".join(words[words.index("send") + 1:contact_index - 1])
        send_whatsapp_message(contact, message)
    
    elif "write a note" in query or "type" in query:
        note_text = query.replace("write a note", "").replace("type", "").strip()
        write_in_notepad(note_text)
    
    elif "open" in query:
        app_name = query.replace("open", "").strip()
        open_app(app_name)
    
    else:
        speak("I didn't understand. Can you rephrase?")
