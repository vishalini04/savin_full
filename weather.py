import datetime
import requests
from speakListen import speak

API_KEY = "your_openweathermap_api_key"

def get_weather(city):
    """Fetches the current date, time, temperature, and weather for a given city."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()

    if response.get("cod") != 200:
        return f"Sorry, I couldn't fetch the weather for {city}. But today is {datetime.datetime.now().strftime('%A, %B %d, %Y')} and the time is {datetime.datetime.now().strftime('%I:%M %p')}."

    temp = response["main"]["temp"]
    weather = response["weather"][0]["description"]
    date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    time = datetime.datetime.now().strftime("%I:%M %p")

    return f"Today is {date}, the time is {time}. The temperature in {city} is {temp}°C with {weather} conditions."
