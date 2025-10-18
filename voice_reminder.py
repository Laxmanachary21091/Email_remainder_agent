import pyttsx3

def speak_reminder(summary, time_str):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    engine.setProperty("volume", 1.0)

    message = f"Hey! Reminder alert. {summary} scheduled at {time_str}."
    print(f"🔊 Speaking: {message}")
    engine.say(message)
    engine.runAndWait()
