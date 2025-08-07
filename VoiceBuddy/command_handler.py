import webbrowser
import requests
import datetime
import pywhatkit
import pyjokes
import subprocess
import os

# Optional: Replace with your actual keys
WEATHER_API_KEY = "your_openweather_api_key"
NEWS_API_KEY = "your_newsapi_key"


def handle_command(command):
    command = command.lower().strip()

    # --- Time ---
    if "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {now}"

    # --- Joke ---
    elif "joke" in command:
        return pyjokes.get_joke()

    # --- Weather ---
    elif "weather" in command:
        return get_weather("delhi")  # Static city for now

    # --- News ---
    elif "news" in command:
        return get_news()

    # --- Open apps/websites ---
    elif "open" in command:
        return open_website_or_app(command)

    # --- Play song ---
    elif "play" in command:
        return play_song(command)

    # --- Fallback for unknown ---
    else:
        return "Sorry, I didn't understand that. Please try again."


# ---------- Helper Functions ----------

def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data["cod"] != 200:
            return "Sorry, I couldn't fetch the weather."
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        return f"The weather in {city} is {desc} with a temperature of {temp}°C."
    except Exception:
        return "Error getting weather."


def get_news():
    try:
        url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"
        response = requests.get(url)
        articles = response.json().get("articles", [])[:5]
        if not articles:
            return "No news found."
        news_list = [f"{i + 1}. {article['title']}" for i, article in enumerate(articles)]
        return "\n".join(news_list)
    except Exception:
        return "Sorry, I couldn't fetch the news."


def open_website_or_app(command):
    if "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"
    elif "google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google"
    elif "gmail" in command:
        webbrowser.open("https://mail.google.com")
        return "Opening Gmail"
    elif "spotify" in command:
        try:
            subprocess.Popen(["C:\\Users\\kshitij\\AppData\\Roaming\\Spotify\\Spotify.exe"])
            return "Opening Spotify app"
        except Exception:
            webbrowser.open("https://open.spotify.com")
            return "Opening Spotify in browser"
    else:
        return "Sorry, I don't know how to open that."


def play_song(command):
    try:
        song_name = command.lower().replace("play", "").strip()
        if song_name:
            pywhatkit.playonyt(song_name)
            return f"Playing {song_name} on YouTube"
        else:
            return "Please tell me the name of the song you want to play."
    except Exception as e:
        return f"Error playing song: {str(e)}"

