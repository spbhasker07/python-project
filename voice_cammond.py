import speech_recognition as sr
import webbrowser
import datetime
import os
from gtts import gTTS
import playsound

def speak_hindi(text):
    tts = gTTS(text=text, lang='hi')
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("pather ke sanam tujhe hamna ")
        try:
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
            content = r.recognize_google(audio, language='hi-IN')
            print("User said:", content)
            return content.lower()
        except sr.UnknownValueError:
            print("समझ नहीं आया, फिर बोलिए")
            return ""
        except Exception as e:
            print(f"Error: {e}")
            return ""

def main_process():
    speak_hindi("Sir ajj kai kya task hai")

    while True:
        request = command()

        if request == "":
            continue

        if "नमस्ते" in request or "हेलो" in request:
            speak_hindi("नमस्ते, बताइए मैं क्या कर सकता हूँ")

        elif "गाना चलाओ" in request:
            speak_hindi("गाना चला रहा हूँ")
            webbrowser.open("https://www.youtube.com")

        elif "समय" in request:
            time = datetime.datetime.now().strftime("%H:%M")
            speak_hindi(f"अभी समय है {time}")

        elif "बंद हो जाओ" in request:
            speak_hindi("ठीक है, अलविदा")
            break

        else:
            speak_hindi("मैं इंटरनेट पर खोज रहा हूँ")
            search_url = f"https://www.google.com/search?q={request.replace(' ','+')}"
            webbrowser.open(search_url)

main_process()
