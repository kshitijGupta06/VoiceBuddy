import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
import requests
import json
from voice_io import speak, listen
from command_handler import handle_command
from llm_response import get_llm_response

def main():
    speak("Hey! I am VoiceBuddy, your personal voice assistant. How can I help you today?")
    
    while True:
        command = listen()

        if not command:
            speak("I didn't catch that. Please say it again.")
            continue

        if "exit" in command or "stop" in command or "quit" in command:
            speak("Goodbye! Have a great day.")
            break

        response = handle_command(command)
        
        # Use local LLM only if fallback message is returned
        if "didn't understand" in response:
            response = get_llm_response(command)
        
        speak(response)

if __name__ == "__main__":
    main()

def run_voicebuddy():
    speak_text("Hi, I'm VoiceBuddy! How can I help you?")

    while True:
        user_input = listen_to_user()

        if not user_input:
            continue

        if "exit" in user_input or "stop" in user_input:
            speak_text("Goodbye, friend!")
            break

        response = handle_command(user_input)

        if response:
            speak_text(response)
        else:
            speak_text("I'm not sure how to help with that.")

if __name__ == "__main__":
    run_voicebuddy()


# Initialize text-to-speech
engine = pyttsx3.init()

def speak(text):
    print("VoiceBuddy:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("User:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Check your internet connection.")
        return ""

# Handle commands
def handle_command(command):
    if "time" in command:
        from datetime import datetime
        time = datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")
    
    elif "open spotify" in command:
        subprocess.Popen(["C:\\Users\\kshitij\\AppData\\Roaming\\Spotify\\Spotify.exe"])
        speak("Opening Spotify")

    elif "play" in command:
        query = command.replace("play", "").strip()
        url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
        speak(f"Playing {query} on YouTube")
        webbrowser.open(url)

    elif "joke" in command:
        response = ollama_ask("Tell me a short joke.")
        speak(response)

    elif "weather" in command:
        city = "Delhi"
        url = f"https://wttr.in/{city}?format=3"
        result = requests.get(url).text
        speak(f"Weather in {result}")

    else:
        response = ollama_ask(command)
        speak(response)

# Get response from local Ollama LLM
def ollama_ask(prompt):
    try:
        res = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "mistral", "prompt": prompt, "stream": False}
        )
        return res.json()['response']
    except Exception as e:
        return "Failed to connect to Ollama."

# Main loop
def main():
    while True:
        command = listen()
        if command:
            handle_command(command)
        if "exit" in command or "quit" in command:
            break

if __name__ == "__main__":
    main()
