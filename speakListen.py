import time
from colorama import Fore, Back, Style
import speech_recognition as sr
import os
import pyttsx3
import datetime
from rich.progress import Progress
import requests



python = pyttsx3.init("sapi5") # name of the engine is set as Python
voices = python.getProperty("voices")
#print(voices)
python.setProperty("voice", voices[1].id)
python.setProperty("rate", 140)


def speak(text):
    """This function would speak aloud some text provided as parameter
    
    Args:
        text ([str]): It is the speech to be spoken
    """    
    python.say(text)
    python.runAndWait()

def get_weather(city):
    """Fetches real-time weather data for a given city."""
    try:
        API_KEY = "148564937d12fae2cf1a1b6acb5f73ad"  # Your actual API key as a string
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            temp = data["main"]["temp"]
            weather_desc = data["weather"][0]["description"]
            return temp, weather_desc
        else:
            return None, None
    except Exception as e:
        print("Error fetching weather:", e)
        return None, None

def tell_time():
    """Speaks the current time."""
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {now}")

def tell_date():
    """Speaks the current date."""
    now = datetime.datetime.now().strftime("%A, %d %B %Y")
    speak(f"Today's date is {now}")

def tell_weather():
    """Asks for city and tells the weather."""
    speak("Please tell me your city for weather updates.")
    city = hear()

    if city.lower() == "none" or not city.strip():
        speak("I couldn't detect the city.")
        return

    temp, weather_desc = get_weather(city)
    if temp:
        speak(f"Currently, it's {temp}°C with {weather_desc} in {city}.")
    else:
        speak("I couldn't fetch the weather.")

def greet(g):
    """Greets the user with current time, date, and weather conditions."""
    if g in ["start", "s"]:
        now = datetime.datetime.now()
        date_str = now.strftime("%A, %d %B %Y")
        time_str = now.strftime("%I:%M %p")
        hour = now.hour

        greeting = "Good Morning" if hour < 12 else "Good Afternoon" if hour < 17 else "Good Evening"
        speak("Please tell me your city for weather updates.")
        city = hear()

        if city.lower() == "none" or not city.strip():
            city = "your location"  # Default fallback if city not detected

        temp, weather_desc = get_weather(city)
        weather_message = f"Currently, it's {temp}°C with {weather_desc} in {city}." if temp else "I couldn't fetch the weather."

        text = f"{greeting}! Today is {date_str}, and the time is {time_str}. {weather_message} I am Savin. How may I assist you?"
        speak(text)

    elif g in ["quit", "end", "over", "e"]:
        speak("Thank you! Goodbye!")

def hear():
    """It will process the speech of user using Google_Speech_Recognizer(recognize_google)

    Returns:
        [str]: Speech of user as a string in English(en - IN)
    """    
    r = sr.Recognizer()
    """Reconizer is a class which has lot of functions related to Speech i/p and o/p.
    """
    r.pause_threshold = 1 # a pause of more than 1 second will stop the microphone temporarily
    r.energy_threshold = 300 # python by default sets it to 300. It is the minimum input energy to be considered. 
    r.dynamic_energy_threshold = True # pyhton now can dynamically change the threshold energy

    with sr.Microphone() as source:
        # read the audio data from the default microphone
        print(Fore.RED + "\nListening...")
        #time.sleep(0.5)

        speech = r.record(source, duration = 9)  
        # option 
        #speech = r.listen(source)
        
        # convert speech to text
        try:
            #print("Recognizing...")
            recognizing()
            speech = r.recognize_google(speech)
            print(speech + "\n")
        
        except Exception as exception:
            print(exception)
            return "None"
    return speech

def recognizing():
    """Uses the Rich library to print a simulates version of "recognizing" by printing a loading bar.
    """
    with Progress() as pr:
        rec = pr.add_task("[red]Recognizing...", total = 100)
        while not pr.finished:
            pr.update(rec, advance = 1.0)
            time.sleep(0.01)

def long_hear(duration_time = 60):
    """It will process the speech of user using Google_Speech_Recognizer(recognize_google)
        the difference between the hear() and long_hear() is that - the
        hear() - records users voice for 9 seconds
        long_hear() - will record user's voice for the time specified by user. By default, it records for 60 seconds.
    Returns:
        [str]: [Speech of user as a string in English(en - IN)]
    """    
    r = sr.Recognizer()
    """Reconizer is a class which has lot of functions related to Speech i/p and o/p.
    """
    r.pause_threshold = 1 # a pause of more than 1 second will stop the microphone temporarily
    r.energy_threshold = 300 # python by default sets it to 300. It is the minimum input energy to be considered. 
    r.dynamic_energy_threshold = True # pyhton now can dynamically change the threshold energy

    with sr.Microphone() as source:
        # read the audio data from the default microphone
        print(Fore.RED + "\nListening...")
        #time.sleep(0.5)

        speech = r.record(source, duration = duration_time)  
        # option 
        #speech = r.listen(source)
        # convert speech to text
        try:
            print(Fore.RED +"Recognizing...")
            #recognizing()
            speech = r.recognize_google(speech)
            #print(speech + "\n")
        
        except Exception as exception:
            print(exception)            
            return "None"
    return speech

def short_hear(duration_time = 5):
    """It will process the speech of user using Google_Speech_Recognizer(recognize_google)
        the difference between the hear() and short_hear() is that - the
        hear() - records users voice for 9 seconds
        short_hear - will record user's voice for 5 seconds. 
    Returns:
        [str]: [Speech of user as a string in English(en - IN)]
    """    
    r = sr.Recognizer()
    """Reconizer is a class which has lot of functions related to Speech i/p and o/p.
    """
    r.pause_threshold = 1 # a pause of more than 1 second will stop the microphone temporarily
    r.energy_threshold = 300 # python by default sets it to 300. It is the minimum input energy to be considered. 
    r.dynamic_energy_threshold = True # pyhton now can dynamically change the threshold energy

    with sr.Microphone() as source:
        # read the audio data from the default microphone
        print(Fore.RED + "\nListening...")
        #time.sleep(0.5)

        speech = r.record(source, duration = duration_time)  # option 
        #speech = r.listen(source)
        # convert speech to text
        try:
            print(Fore.RED +"Recognizing...")
            #recognizing()
            speech = r.recognize_google(speech)
            #print(speech + "\n")
        
        except Exception as exception:
            print(exception)            
            return "None"
    return speech

        

if __name__ == '__main__':
    # print("Enter your name")
    # name = hear()
    # speak("Hello " + name)
    # greet("s")
    # greet("e")
    pass
    #hear()
    #recognizing()
    