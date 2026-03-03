from speech_input import take_command
from speech_output import speak
from ml_model import predict_action
from task_executor import execute_task

def main():
    speak("Hello! I am your AI voice assistant.")
    while True:
        command = take_command()
        if command == "none":
            continue
        if "exit" in command or "bye" in command:
            speak("Goodbye!")
            break
        try:
            action = predict_action(command)
            execute_task(action)
        except:
            speak("Sorry, I couldn't process that.")

if __name__ == "__main__":
    main()