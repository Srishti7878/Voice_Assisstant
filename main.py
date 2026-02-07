import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import threading

def recognize_speech():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            result_label.config(text="Listening...", fg="blue")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            result_label.config(text="Recognizing...", fg="orange")
            text = recognizer.recognize_google(audio)
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, text)
            result_label.config(text="Recognition Complete ✅", fg="green")
    except sr.UnknownValueError:
        result_label.config(text="Couldn't understand the audio ❌", fg="red")
    except sr.RequestError as e:
        result_label.config(text=f"API Error: {e}", fg="red")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}", fg="red")

def start_recognition_thread():
    thread = threading.Thread(target=recognize_speech)
    thread.start()

# GUI Setup
root = tk.Tk()
root.title("🎤 Speech to Text App")
root.geometry("500x400")
root.resizable(False, False)
root.configure(bg="#f4f4f4")

title_label = tk.Label(root, text="Speech to Text", font=("Arial", 20, "bold"), bg="#f4f4f4", fg="#333")
title_label.pack(pady=10)

start_button = tk.Button(root, text="Start Listening", font=("Arial", 14), bg="#4CAF50", fg="white", padx=20, pady=10, command=start_recognition_thread)
start_button.pack(pady=10)

result_label = tk.Label(root, text="Press the button and speak", font=("Arial", 12), bg="#f4f4f4", fg="gray")
result_label.pack(pady=5)

result_text = tk.Text(root, height=10, width=50, font=("Consolas", 12), wrap=tk.WORD)
result_text.pack(pady=10)
result_text.config(state=tk.NORMAL)

# Footer
footer_label = tk.Label(root, text="Created with ❤️ using Python", font=("Arial", 10), bg="#f4f4f4", fg="gray")
footer_label.pack(pady=5)

root.mainloop()
