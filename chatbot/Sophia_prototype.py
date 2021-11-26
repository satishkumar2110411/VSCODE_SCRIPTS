#REQUIRED IMPORTS
import os
import datetime
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
from random import choice,random
from responses import *
import subprocess

#REQUIRED FUNCTIONS
def speak(text):
    tts = gTTS(text=text , lang = "en", tld = 'co.uk')
    try:
        filename = "G:\VSCODE_SCRIPTS\chatbot\\audio_files\\voice.mp3"
        tts.save(filename)
    except Exception:
        os.remove("G:\VSCODE_SCRIPTS\chatbot\\audio_files\\voice.mp3")
        filename = "G:\VSCODE_SCRIPTS\chatbot\\audio_files\\voice.mp3"
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

def note(text):
    date = str(datetime.datetime.now())[0:19]
    print(date)
    file_name = date.replace(':',"-")+'-note.txt'
    with open('G:\VSCODE_SCRIPTS\chatbot\\notes\\'+file_name,'w+') as f:
        f.write(text)
    
    subprocess.Popen(['notepad.exe',file_name])
#BOOTING UP SOPHIA

note('hi')