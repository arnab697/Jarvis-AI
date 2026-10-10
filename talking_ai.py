import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return None

# Main Loop
if __name__ == "__main__":
    speak("Hello! How can I help you?")
    while True:
        user_input = listen()
        if user_input:
            if "exit" in user_input.lower():
                speak("Goodbye!")
                break
            speak(f"You said: {user_input}")
