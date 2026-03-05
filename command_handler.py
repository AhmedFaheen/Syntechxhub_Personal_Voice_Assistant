from speech_engine import speak
from actions import *


def handle_command(command):

    if "open youtube" in command:
        open_youtube()

    elif "open google" in command:
        open_google()

    elif "search" in command:
        search_web(command)

    elif "time" in command:
        tell_time()

    elif "open notepad" in command:
        open_notepad()

    elif "open calculator" in command:
        open_calculator()

    elif "help" in command:
        speak("You can ask me to open youtube, search the web, tell the time, or open applications.")

    elif "exit" in command or "stop" in command:
        speak("Goodbye")
        exit()

    elif command != "":
        speak("Command not recognized.")