import speech_recognition as sr
import pyttsx3
import threading
import pyjokes
import pywhatkit
from datetime import datetime
import webbrowser
import queue
import time
import requests
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def ask_ollama(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",  # or llama3, gemma, etc.
                "prompt": prompt,
                "stream": False
            }
        )
        data = response.json()
        return data.get("response", "I couldn't find the answer.")
    except Exception as e:
        print(f"Error contacting Ollama: {e}")
        return "I had trouble connecting to Ollama. Please make sure it's running."


# Queue to serialize speech
speech_queue = queue.Queue()


def speak_text(text):
    def run():
        try:
            engine.say(text)
            engine.runAndWait()
        except RuntimeError as e:
            print(f"[Speech Error] {e}")
    threading.Thread(target=run).start()

def speech_loop():
    while True:
        text = speech_queue.get()
        if text:
            engine.say(text)
            engine.runAndWait()
        speech_queue.task_done()

# Start the speech thread
speech_thread = threading.Thread(target=speech_loop, daemon=True)
speech_thread.start()

def speak_text(text):
    print(f"VoiceBuddy: {text}")
    speech_queue.put(text)

def handle_command(command):
    command = command.lower()

    if "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"

    elif "play" in command:
        song_name = command.replace("play", "").strip()
        if song_name:
            speak_text(f"Playing {song_name} on YouTube")
            pywhatkit.playonyt(song_name)
            return f"Playing {song_name} on YouTube"
        else:
            return "What song should I play?"

    elif "time" in command:
        time = datetime.now().strftime("%I:%M %p")
        return f"The time is {time}"

    elif "weather" in command:
        return "Weather feature coming soon!"

    elif "joke" in command:
        return pyjokes.get_joke()

    elif "what is" in command or "who is" in command or "define" in command:
        return "That's an interesting question. I suggest looking it up on Google or Wikipedia. Integration with ChatGPT or Wolfram Alpha coming soon."

    else:
        return "Sorry, I didn't understand that command."


def listen_to_user():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio)
        print(f"User: {user_input}")
        return user_input.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        print("Speech service unavailable.")
        return ""


def ask_ollama(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",  # or llama3, gemma, etc.
                "prompt": prompt,
                "stream": False
            }
        )
        data = response.json()
        return data.get("response", "I couldn't find the answer.")
    except Exception as e:
        print(f"Error contacting Ollama: {e}")
        return "I had trouble connecting to Ollama. Please make sure it's running."
