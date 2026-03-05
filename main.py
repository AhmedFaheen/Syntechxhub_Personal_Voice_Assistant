from speech_engine import listen, speak
from command_handler import handle_command


def main():

    speak("Hello. I am your personal voice assistant.")

    while True:

        command = listen()

        handle_command(command)


if __name__ == "__main__":
    main()