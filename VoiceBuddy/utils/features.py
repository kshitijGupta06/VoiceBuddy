import datetime
import pyjokes
import webbrowser
import random
import requests

def tell_time():
    return "The current time is " + datetime.datetime.now().strftime("%I:%M %p")

def crack_joke():
    return pyjokes.get_joke()

def open_youtube():
    webbrowser.open("https://www.youtube.com")
    return "Opening YouTube."

def open_spotify():
    webbrowser.open("https://open.spotify.com")
    return "Opening Spotify."

def play_random_song():
    songs = [
        "https://open.spotify.com/track/7GhIk7Il098yCjg4BQjzvb",
        "https://open.spotify.com/track/0VjIjW4GlUZAMYd2vXMi3b",
        "https://open.spotify.com/track/3dYD57lRAUcMHufyqn9GcI"
    ]
    webbrowser.open(random.choice(songs))
    return "Playing a random song on Spotify."

def get_weather():
    # Replace with your city or get dynamically
    city = "Delhi"
    api_key = "your_openweathermap_api_key"  # 🔐 get from https://openweathermap.org/
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url).json()
        if response.get("main"):
            temp = response['main']['temp']
            desc = response['weather'][0]['description']
            return f"The current weather in {city} is {desc} with a temperature of {temp}°C."
        else:
            return "Sorry, I couldn't fetch the weather."
    except Exception:
        return "Error fetching weather. Please try again later."

def get_news():
    api_key = "your_newsapi_key"  # 🔐 get from https://newsapi.org/
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"

    try:
        response = requests.get(url).json()
        articles = response.get("articles", [])[:3]
        if not articles:
            return "No news found."
        return "Here are the top news headlines: " + " | ".join([article['title'] for article in articles])
    except Exception:
        return "Error fetching news."
