import datetime
import os
import platform
import subprocess
import webbrowser

import pyttsx3
import requests
import speech_recognition as sr

from . import config
from . import analytics

# State collected during a session
time_queries = []
query_lengths = []
query_words = []
query_texts = []
user_intents = []

# Initialize TTS engine (let pyttsx3 choose the best driver for the platform)
engine = pyttsx3.init()
voices = engine.getProperty("voices")
if voices:
    engine.setProperty('voice', voices[0].id)


def speak(text: str):
    engine.say(text)
    engine.runAndWait()


def take_command(timeout=5, phrase_time_limit=8):
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
    except Exception as e:
        print("Microphone not available or timed out:", e)
        return None

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
        return query
    except Exception as e:
        print("Unable to Recognize your voice:", e)
        return None


def detect_intent(query: str) -> str:
    q = query.lower()
    if "open youtube" in q:
        return "Open YouTube"
    if "open google" in q:
        return "Open Google"
    if "play music" in q:
        return "Play Music"
    if "time" in q:
        return "Get Time"
    if "exit" in q or "quit" in q:
        return "Exit"
    if "how are you" in q:
        return "Ask How Are You"
    if "who made you" in q:
        return "Ask Who Made You"
    if "joke" in q:
        return "Ask for Joke"
    if "your work" in q:
        return "Ask About Your Work"
    if "when were you created" in q:
        return "Ask When You Were Created"
    return "Unknown"


def open_music_file(path: str):
    if not path or not os.path.exists(path):
        speak("Music file not found. Please set MUSIC_FILE_PATH environment variable or update the path.")
        return
    system = platform.system()
    if system == "Windows":
        os.startfile(path)
    elif system == "Darwin":
        subprocess.call(["open", path])
    else:
        subprocess.call(["xdg-open", path])


def weather_info(city: str = "Solapur"):
    # Use config; do not crash if key missing here, let caller decide
    if not config.OPENWEATHER_API_KEY:
        speak("OpenWeather API key not configured. Please set OPENWEATHER_API_KEY.")
        return

    params = {"q": city, "appid": config.OPENWEATHER_API_KEY}
    try:
        r = requests.get(config.BASE_URL, params=params, timeout=5)
        r.raise_for_status()
        weather_data = r.json()
        if weather_data.get("cod") != 200 and weather_data.get("cod") != "200":
            speak("City not found or API error.")
            return
        weather_description = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]
        speak(f"The weather in {city} is {weather_description}. The temperature is {temperature} Kelvin.")
    except Exception as e:
        print("Weather lookup failed:", e)
        speak("Unable to fetch weather data.")


def start_assistant():
    speak("I'm ready to assist you.")
    while True:
        query = take_command()
        if query is None:
            # recognition failed, skip iteration (do not record "None")
            continue

        query_texts.append(query)
        q_lower = query.lower()
        time_queries.append(datetime.datetime.now())
        query_lengths.append(len(query))
        query_words.extend(query.split())

        intent = detect_intent(query)
        user_intents.append(intent)

        # Actions
        if "open youtube" in q_lower:
            speak("Here you go to YouTube")
            webbrowser.open("https://www.youtube.com")
        elif "open google" in q_lower:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
        elif "play music" in q_lower:
            music_path = config.MUSIC_FILE_PATH
            if music_path:
                open_music_file(music_path)
            else:
                speak("No music file configured. Please set MUSIC_FILE_PATH.")
        elif "time" in q_lower:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif "exit" in q_lower or "quit" in q_lower:
            speak("Thanks for using the assistant.")
            break
        elif "how are you" in q_lower:
            speak("I am fine, Thank you.")
        elif "who made you" in q_lower:
            speak("I have been created by shraddha, namrata, and vidya.")
        elif "joke" in q_lower:
            speak("Here's a joke for you: Why don't scientists trust atoms? Because they make up everything!")
        elif "your work" in q_lower:
            speak("I'm here to assist you with various tasks such as providing information, playing music and more.")
        elif "when were you created" in q_lower:
            speak("I was created on October 25th, 2023.")
        else:
            speak("I don't have an answer for that. Please provide more specific commands.")

    # On exit: run analytics (pass collected lists)
    try:
        analytics.analyze_time_queries(time_queries)
        analytics.analyze_query_lengths(query_lengths)
        analytics.analyze_query_words(query_words)
        analytics.analyze_user_intents(user_intents)
        analytics.analyze_query_length_vs_word_count(query_texts)
    except Exception as e:
        print("Analytics failed:", e)
