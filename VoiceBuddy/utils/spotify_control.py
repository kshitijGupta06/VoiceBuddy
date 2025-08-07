# utils/spotify_control.py

import subprocess
import pyautogui
import time

def play_song(song_name="Saiyaara"):
    try:
        # Step 1: Open Spotify
        subprocess.Popen("spotify")  # This assumes Spotify is in PATH
        time.sleep(5)  # Wait for Spotify to open

        # Step 2: Simulate search and play
        pyautogui.hotkey("ctrl", "l")  # Go to search bar
        time.sleep(1)
        pyautogui.write(song_name)
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(3)
        pyautogui.press("tab", presses=3, interval=0.5)
        pyautogui.press("enter")
        return f"Playing {song_name} on Spotify."
    except Exception as e:
        return f"Failed to play on Spotify: {str(e)}"
