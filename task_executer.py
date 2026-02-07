import webbrowser
import os
import datetime
from speech_output import speak

def execute_task(action):
    if action == "open_google":
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")
    elif action == "search_youtube":
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")
    elif action == "play_music":
        try:
            os.startfile("C:\\Users\\Public\\Music\\Sample Music\\Kalimba.mp3")  # Adjust path
            speak("Playing music.")
        except:
            speak("Could not find the music file.")
    elif action == "get_time":
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {current_time}.")
    elif action == "tell_joke":
        speak("Why don’t scientists trust atoms? Because they make up everything!")
    elif action == "get_weather":
        speak("It’s 29 degrees Celsius and sunny today.")  # Static or API can be used
    elif action == "open_notepad":
        os.system("notepad")
        speak("Opening Notepad.")
    else:
        speak("Sorry, I don't know how to do that.")
