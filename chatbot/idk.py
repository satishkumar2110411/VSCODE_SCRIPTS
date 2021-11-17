import os
import datetime
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
from random import choisezzz
from responses import *

def speak(text):
    tts = gTTS(text=text , lang = "en", tld = 'co.uk')
    try:
        filename = "voice.mp3"
        tts.save(filename)
    except Exception:
        os.remove("voice.mp3")
        filename = "voice.mp3"
        tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        audio = listener.listen(source)
        said =''
        try:
            said = listener.recognize_google(audio)
        except Exception as e:
            print(str(e))
    return(said)

while True:
    text = get_audio()
    print('Recieved Input: '+ text)
    if text == '':
        continue
    elif "sophia" in text.lower() or "sofia" in text.lower():
        response = initialise[randint(0,len(initialise)-1)] + introduction[randint(0,len(introduction)-1)]
        speak(response)
        continue
    elif "bye" in text.lower():
        statement = end[randint(0,len(end)-1)]
        hour = datetime.datetime.now().hour
        if hour<21:
            speak(statement+" Have a great day ahead!")
        else:
            speak(statement+" Good night")
        break
    else:
        speak("I'm not sure I quite understood what you said.")
        continue
    
