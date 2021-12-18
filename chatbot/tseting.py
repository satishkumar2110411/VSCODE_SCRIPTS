#REQUIRED IMPORTS
import os
import datetime
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
from random import choice,random
from responses import *

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

#BOOTING UP SOPHIA

#GLOBAL VARIABLES
hour = datetime.datetime.now().hour
tolerance = 90
path="G:\VSCODE_SCRIPTS\chatbot\Music_for_Sophia"
files=os.listdir(path)
music =[]
for i in files:
    if '.mp3' in i:
        music += [i,]

#QUESTION RESPONSE SESSION
i = 0

while True:
    while i == 0: #initialising sequence
        intro = get_audio().lower().split()
        if "sophia wake up" in intro or "up" in intro or "turn on" in intro or "wake up" in intro:
            i = 1
            intro_phrase = choice(initialise)+choice(introduction)
            speak(intro_phrase)
    
    print('Listening....')
    Text = get_audio() #RECIEVING MICROPHONE INPUT
    print('Recieved Input: '+ Text)
    text = Text.lower()
    self_talk_percent = (100-tolerance)/100

    if text == '' and random() < self_talk_percent :   # NO RESPONSE
        response = choice(idle)
        print(response)
        
        if response == 'shutdown':
            statement = choice(end)
            if hour<21:
                speak(statement+" Have a great day ahead!")
            else:
                speak(statement+" Good night")
            break
        
        elif response == '':
            pass
        
        elif response == 'cricket noises':
            playsound.playsound("G:\VSCODE_SCRIPTS\chatbot\\audio_files\crickets.mp3")
        
        elif response == "humming sounds":
            playsound.playsound("G:\VSCODE_SCRIPTS\chatbot\\audio_files\\astra humming.mp3")
        
        elif response == 'random song':
            d=choice(music)
            speak("I'm getting bored. Playing "+d)
            os.startfile("G:\VSCODE_SCRIPTS\chatbot\Music_for_Sophia\\"+d)

        else:
            speak(response)
    
    if 'sophia' in text or 'sofia' in text: #recognizing sophia in audio for subsequent response
        
        if 'set tolerance' in text:
            
            new_tolerance = text.split()[-1]
            if new_tolerance == 'zero':
                tolerance = 0
                speak(str(tolerance))
            
            else:
                tolerance = float(new_tolerance)
                if tolerance > 100:
                    tolerance = tolerance%100
                speak(str(tolerance))
            
        elif 'do you like' in text:
            response = choice(do_you_like)
            speak(response)

        elif 'repeat' in text:
            speak('Okay, I am listening.... please speak in 3 seconds')
            response = get_audio()
            speak(response)
        
        elif 'about yourself' in text or 'introduce' in text:
            speak(description)
    
        elif 'age' in text.split() or 'old' in text.split():
            speak(age)
    
        elif 'who made' in text or 'who created' in text or 'creator' in text.split():
            response = choice(creator)
            speak(response)
    
        elif 'how do you work' in text or 'function' in text or 'work' in text.split():
            speak(work_how)

        elif 'flip' in text.split() or 'coin' in text.split():
            speak("It's a "+coin)
    
        elif 'dice' in text.split() or 'die' in text.split():
            speak("You got a "+dice)
    
        elif 'hobby' in text.split() or 'hobbies' in text:
            response = choice(hobby)
            speak(response)
    
        elif "song" in text.split():
            if "favourite" not in text:    
                try:
                    d=choice(music)
                    os.startfile("G:\VSCODE_SCRIPTS\chatbot\Music_for_Sophia\\"+d)
                    speak("Playing "+d)
                except:
                    speak("No songs for you now")
            else:
                try:
                    os.startfile("G:\VSCODE_SCRIPTS\chatbot\Music_for_Sophia\\alvaro_sofia.mp3")
                    speak("This is my favourite song, smiley")
                except:
                    speak("Not in the mood")
        
        elif "bye" in text or "bhai" in text or "by" in text.split() or 'good night' in text: # SHUTDOWN SYSTEM
            statement = choice(end)
        
            if hour<21:
                speak(statement+" Have a great day ahead!")
            else:
                speak(statement+" Good night")
            break

        elif ("rule" in text.split() and "robots" in text.split()):
            statement = choice(rule_the_world)
            speak(statement)

        else: # NON-COMPREHENSIBLE STUFF
            speak("I'm not sure I quite understood what you said.")
            continue

    else:
        if random() > 0.01:
            pass
        else:
            if bool(text) != 0:
                speak("If you want to talk to me, please tell my name. I am very stubborn.")
            pass
                
    
