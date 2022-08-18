import pyttsx3
import os
import random
import datetime
from datetime import datetime
import webbrowser
import msvcrt as m
import requests
from bs4 import BeautifulSoup
import weathercom
import json
import pygame
from time import sleep


def wait():
    m.getch()


APRIL = pyttsx3.init('sapi5')
voice = APRIL.getProperty('voices')
assistant_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enUS_EvaM'
rate = APRIL.getProperty('rate')
APRIL.setProperty('rate', 170)
voices = APRIL.getProperty('voices')
APRIL.setProperty('voice', assistant_voice_id)


def speak(audio):
    APRIL.say(audio)
    APRIL.runAndWait()








def code():

 while True:
    main = input("you:")

    a1=["hi","hello","hey"]
    a2=["time","current time"]
    a3=["google",]
    a4=["add"]
    a5=["switch to offline voice mode","switch1"]
    a6=["subtract"]
    a7=["multiply"]
    a8=["divide"]
    a9=["what is the month"]
    a10=["what is the date"]
    a11=["bye","break","exit"]
    a12=["hack bitcoin","hack BTC"]
    a13=["track iss"]
    a14=["count asteroids"]
    a15=["switch to online voice mode",'switch2']
    #a16=["alarm"]
    a17=["music"]
    a18=['music2']
    a19=["stone"]
    a20=["paper"]
    a21=["scissor"]
    a22=["stone",'paper','scissor']
    a23=["let's play a game"]




    if main in a1:
        rand=random.choice(a1)
        speak(rand)
    elif main in a2:
        now=datetime.now()
        l1 = current_time=now.strftime("%H:%M")
        print("the time is")
        print(l1)
        speak("the time is") or speak(current_time)

    elif main in a3:
        get=webbrowser.open("www.google.com",new=2)

    elif main in a4:
        first_number=input("enter first number:")
        second_number=input("enter second number:")
        result = float(first_number) + float(second_number)
        speak(result)

    elif main in a5:
        speak(f'switching to offline voice mode')

        from main import asmit

        asmit()



    elif main in a6:
        first_number = input("enter first number:")
        second_number = input("enter second number:")
        result = float(first_number) - float(second_number)
        speak(result)

    elif main in a7:
        first_number = input("enter first number:")
        second_number = input("enter second number:")
        result = float(first_number) * float(second_number)
        speak(result)

    elif main in a8:
        first_number = input("enter first number:")
        second_number = input("enter second number:")
        result = float(first_number) / float(second_number)
        speak(result)

    elif main in a9:
        now=datetime.now()
        current_time=now.strftime("m")
        speak("it is the month of") or speak(current_time)

    elif main in a10:
        now=datetime.now()
        current_time=now.strftime("%h")
        speak("today is") or speak(current_time)



    elif main in a11:
        speak("going to sleep")
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load('fg.mp3')
        pygame.mixer.music.play()
        sleep(2)
        exit()


    elif main in a12:
        speak("ok i am playing music")
        music_dir = 'C:\\Users\\asmid\\Documents\\music'
        musics = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, musics[0]))

    elif main in a14:
        speak(f'connecting to NASA')
        try:
            from Nasa import Astro
            speak("tell me the starting date sir!")
            start = input("Enter the starting date :")
            speak("tell me the end date.")
            end = input("Enter the ending date :")
            Astro(start, end)

        except:
            speak("Can't connect to NASA's computer")
            print("")

    elif main in a13:
        speak(f'connecting to NASA')
        try:
         from Nasa import IssTracker

         IssTracker()
        except:
            speak("Can't connect to NASA's computer")
            print("")

    elif main in a15:
          from module_onl import asmi
          asmi()




    elif main in a17:
        speak(f'This is some music for you, hope you enjoy')
        os.startfile('arcade.mp3')
    elif main in a18:
        speak(f'This is some music for you, hope you enjoy')
        os.startfile('kn.mp3')
    elif main in a19:
        rand = random.choice(a22)
        speak(rand)
        print(rand)
    elif main in a20:
        rand = random.choice(a22)
        speak(rand)
        print(rand)
    elif main in a21:
        rand = random.choice(a22)
        speak(rand)
        print(rand)

    elif main in a23:
       print("let's play")
       speak("ok , let's play ,    stone, paper and scissor.  i will chose")
       rand = random.choice(a22)
       speak(rand)
       print(rand)



code()



