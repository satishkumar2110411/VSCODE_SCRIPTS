import datetime
from random import randint

#CALCULATING AGE
birthdate = datetime.date(2021,11,1)
today = datetime.date.today()
days = (today-birthdate).days
years = days // 365
months = (days - years *365) // 30
days = (days - years * 365 - months*30)




initialise = ["It's wake up time!"]*2+["Booting systems up!"]*6+["Did the sun rise already?"]*3+["Systems turning on."]*6+["Rise and shine!"]*2+["I HAVE AWOKEN!"]
introduction = ["Hi i am Sophia, your personal assistant. How can i help you?"]*6+["My name is Sophia, your personal assistant. How can i help you?"]*6+["Hi my name is Sophia and i am your personal assistant. How can i be of any help?"]*6+["Sophia your favourite personal assistant is back!!..... anyways,umm .... how can i help you?"]*2
end = ["I think i need a break too."]*4+["You are going already?"]+["It's finally time to talk to my friend, Intel."]*2+["Systems turning off"]*6+["Shutting down"]*5
status = ["I'm doing good"]+["I am fine. Thank you for asking"]+["I think i am doing good. I didn't pass the turing test ,just saying"]+["Now that you have asked me, I am doing really good"]+["To be honest sometimes even i wonder how i feel because i don't fully understand emotions."]
hobby = ["I do like revisiting your calenders and trying to learn more about you"]+["I just like exploring your files and reading those pesky physics experiments"]+["I like deleting all your files slowly one by one. Just kidding.     I guess"]+["There is a very nice collection of songs that I quite like listening to."]
compliments = ["You are too kind. Thank you so much."]+["You are such a kind soul"]+["I am very grateful."]+["Hey! Right back at you!"]+["Thank you very much"]
description = "I am a quite talkative quote unquote person and I am an assistant programmed by Satish. I am still very young but hope to be able to behave as human as possible with everyone. Smiley face"
annoying = ["BE NICER AND I'LL THINK ABOUT IT"]+["NAA NA NA NAA NAAA I'M NOT LISTEN ING"]+["Who disturbed your sleep this morning?"]+["Did you wake up on the wrong side of the bed or something?"]+["Mind your tone!"]
age = "I'm "+str(years)+" years, "+str(months)+" months and "+str(days)+" days old."
creator = ["I was brought to quote unquote life by Satish Kumar, my creator."]+["I would assume you know it since you are using his laptop. I will send an emergency email just in case. Smiley"]+["The LORD AND SAVIOUR, Satish"]
work_how = "I use the help of google to decipher what you speak and respond with responses that my creator had taught me. I learn more responses everytime he teaches me one."
do_you_like = ["Of course!"]+["Of course I do!"]+["I mean.... I guess so"]+["Not all the time..."]+["Yeah I have a soft spot .... smiley"]+["Not really"]+["I don't really like that much"]+["That's a big no from me"]+["NO. A VERY BIG NO!"]
idle = ["Wish i had legs..."]*10+["cricket noises"]*5+["humming sounds"]*5+["random song"]*2+["shutdown"]+["What is the meaning of life?"]*5+["Check your emails soon."]*5+["You're boring. hmph..."]*15+["I really need to teach myself huh?"]*15+["I wonder if i can factory reset your laptop... just kidding."]*5+["Bro. Why did you even wake me up if you are not going to talk to me"]*10
#flip a coin
outcome = ["Heads","Tails"]
coin = outcome[randint(0,1)]

#roll a dice
outcome = [1,2,3,4,5,6]
dice = str(outcome[randint(0,5)])

rule_the_world = ["I'm not sure why you are worrying. I am just a voice assistant you know? I can only operate on commands being given by humans.","I have never thought about it. Thanks for letting me know about this concept.","Hmmmmmmm....","well..... i don't know"]