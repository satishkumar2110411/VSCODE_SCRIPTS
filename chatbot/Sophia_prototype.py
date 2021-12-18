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

def set_tolerance_reply():
    try:
        new_tolerance = text[-1]
        testing = float(new_tolerance)
    except:
        return
    if new_tolerance == 'zero':
            tolerance = 0
            speak(str(tolerance))
            
    else:
        tolerance = float(new_tolerance)
        if tolerance > 100:
            tolerance = tolerance%100
        speak(str(tolerance))
    return

def like_reply():
    response = choice(do_you_like)
    speak(response)
    return

def repeat_reply():
    speak('Okay, I am listening.... please speak in 3 seconds')
    response = get_audio()
    if response == '':
        speak('That was rude')
    else:
        speak(response)
    return

def introduction_reply():
    speak(description)
    return

def age_reply():
    speak(age)
    return

def creator_reply():
    response = choice(creator)
    speak(response)
    return

def work_reply():
    speak(work_how)
    return

def flip_reply():
    speak('It\'s a '+ coin)
    return

def dice_reply():
    speak('You got a '+ dice)
    return

def hobby_reply():
    response = choice(hobby)
    speak(response)
    return

def song_reply():
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
    return

def bye_reply():
    statement = choice(end)
        
    if hour<21:
        speak(statement+" Have a great day ahead!")
    else:
        speak(statement+" Good night")
    return

def rule_reply():
    statement = choice(rule_the_world)
    speak(statement)
    return


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

    reply = {'tolerance':set_tolerance_reply,
        'like':like_reply,
        'repeat':repeat_reply,
        'yourself':introduction_reply,'introduce':introduction_reply,
        'age':age_reply,'old':age_reply,
        'made':creator_reply,'created':creator_reply,'creator':creator_reply,'invented':creator_reply,
        'work':work_reply,'function':work_reply,
        'flip':flip_reply,'coin':flip_reply,
        'dice':dice_reply,'die':dice_reply,
        'hobby':hobby_reply,'hobbies':hobby_reply,
        'song':song_reply,
        'bye':bye_reply,'bhai':bye_reply,'by':bye_reply,'goodbye':bye_reply,
        'rule':rule_reply,'robots':rule_reply}
    
      
    keywords = list(reply.keys())

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
    
    if 'sophia' in text.split() or 'sofia' in text.split(): #recognizing sophia in audio for subsequent response
        
        for key in text.split():
            if key in keywords:
                reply[key]
                break
            else:
                continue
        
        else: # NON-COMPREHENSIBLE STUFF
            speak("I'm not sure I quite understood what you said.")
            continue

        if ('bye' in text or 'by' in text.split() or 'bhai' in text or 'goodbye' in text):
            break

    else:
        if random() > 0.01:
            pass
        else:
            if bool(text) != 0:
                speak("If you want to talk to me, please tell my name. I am very stubborn.")
            pass
                
    
