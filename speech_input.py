import speech_recognition as sr

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)
    try:
        print("🧠 Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("❌ Could not understand audio.")
        return "none"
    except sr.RequestError:
        print("🔌 Network error.")
        return "none"
