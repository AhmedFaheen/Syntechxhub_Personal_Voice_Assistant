import webbrowser
import datetime
import os
from speech_engine import speak


def open_youtube():
    speak("Opening YouTube")
    webbrowser.open("https://youtube.com")


def open_google():
    speak("Opening Google")
    webbrowser.open("https://google.com")


def search_web(command):
    query = command.replace("search", "")
    speak(f"Searching for {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")


def tell_time():
    time = datetime.datetime.now().strftime("%H:%M")
    speak(f"The time is {time}")


def open_notepad():
    speak("Opening Notepad")
    os.system("notepad")


def open_calculator():
    speak("Opening Calculator")
    os.system("calc")