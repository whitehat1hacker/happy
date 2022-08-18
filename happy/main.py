from vosk import Model, KaldiRecognizer
import pyttsx3
import datetime
from playsound import playsound
import pyaudio
import json
import os
import msvcrt as m
import webbrowser
import pyjokes
# import wikipedia
import random
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
    print('APRIL: ' + audio)
    APRIL.say(audio)
    APRIL.runAndWait()

k1=["loading data, this may take some time","loading models, this usualy take some time"]
rand=random.choice(k1)
speak(rand)



def time():
    Time = datetime.datetime.now().strftime('%I:%M: %p')
    speak('It is')
    speak(Time)


def date():
    today = datetime.datetime.now().strftime(
        'the date today is %d %m %Y, please notice that the format is day, month, year')
    speak(today)


def welcome():
    hour = datetime.datetime.now().hour
    if hour >= 3 and hour < 12:
        speak('Good morning sir. it is a great day today')
        Time = datetime.datetime.now().strftime('%I %M %p')
        speak('the time is')
        speak(Time)


    elif hour >= 12 and hour < 18:
        speak('Good afternoon sir')
        Time = datetime.datetime.now().strftime('%I %M %p')
        speak('the time is')
        speak(Time)

    elif hour >= 18 and hour < 20:
        speak('Good evening sir')
        Time = datetime.datetime.now().strftime('%I %M %p')
        speak('the time is')
        speak(Time)
    elif hour >= 20 and hour < 22:
        Time = datetime.datetime.now().strftime('%I %M %p')
        speak('the time is')
        speak(Time)
        speak('how can i help you sir ')


    elif hour >= 22 and hour < 3:
        speak('It is late sir, let us take a nap')
        speak('it is')
        Time = datetime.datetime.now().strftime('%I %M: %p')
        speak(Time)
        speak('How can I help you now')
        print('')
        print('listening ...')
        print('')


model = Model(r"C:\Users\asmid\PycharmProjects\vosk\vosk-model-en-in-0.5\vosk-model-en-in-0.5")
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('fg.mp3')
pygame.mixer.music.play()
sleep(2)

os.system('cls')
welcome()


rec = KaldiRecognizer(model, 16000)

cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()



a = 0




def asmit():
 while True:
    data=stream.read(4000, exception_on_overflow=False)
    if len(data)==0:
        break
    if rec.AcceptWaveform(data):
        result=rec.Result()
        result=json.loads(result)
        print('Recognized text: ' + result['text'])
        if "hello" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Recognized text: ' + result['text'])
            speak('Hello my boss, how can I help you?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')
        elif "time" in result['text']:
            Time = datetime.datetime.now().strftime('%I %M: %p')
            speak('It is')
            speak(Time)
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "online" in result['text']:
            speak("switching to online mode")
            try:
              from module_onl import js

              js()
            except:
                speak("network connection error")
        elif 'music' in result['text']:
            speak("playing music from pc")
            music_dir = 'C:\\Users\\asmid\\Documents\\music'
            musics = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, musics[0]))

        elif "date" in result['text']:
            today = datetime.datetime.now().strftime('%h')
            speak(today)
            stream.start_stream()
            print('')
            print('listening ...')
            print('')
        elif "hi" in result['text']:
            rand = random.choice("hi""hello""hey")
            speak(rand)
            print('')
            print('listening ...')
            print('')
        elif "let's play" in result["text"]:
            a22=["stone",'paper','scissor']
            print("let's play")
            speak("ok , let's play ,    stone, paper and scissor.  i will chose")
            rand = random.choice(a22)
            speak(rand)
            print(rand)

        elif "stone" in result['text']:
            a1=['paper','scissor','stone']
            rand = random.choice(a1)
            speak(rand)
            print('')
            print('listening ...')
            print('')
        elif "paper" in result['text']:
            a2 = ['paper', 'scissor', 'stone']
            rand = random.choice(a2)
            speak(rand)
            print('')
            print('listening ...')
            print('')
        elif "scissor" in result['text']:
            a3 = ['paper', 'scissor', 'stone']
            rand = random.choice(a3)
            speak(rand)
            print('')
            print('listening ...')
            print('')

        elif "month" in result['text']:
            today = datetime.datetime.now().strftime('%m')
            speak(today)
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "who are you" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Recognized text: ' + result['text'])
            speak('Hi, I am your virtual assistant. How can I help you now, sir?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "April" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Recognized text: ' + result['text'])
            speak('yes sir')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "who made you" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Recognized text: ' + result['text'])
            speak('asmit created me. Is there something else you need me to help you with?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "who make you" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Recognized text: ' + result['text'])
            speak('asmit created me. Is there something else you need me to help you with?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "who created you" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Recognized text: ' + result['text'])
            speak('asmit created me. Is there something else you need me to help you with?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "hack bitcoin" in result['text']:
            speak(f'loading data')
            from bit import hack

            hack()
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "add" in result or "addition" in result['text']:
            speak("first_number")
            first_number = input("enter first number:")
            speak("second_number")
            second_number = input("enter second number:")
            result = float(first_number) + float(second_number)
            speak(result)

        elif "subtract" in result['text']:
            first_number = input("enter first number:")
            second_number = input("enter second number:")
            result = float(first_number) - float(second_number)
            speak(result)
        elif "multiply" in result['text']:
            first_number = input("enter first number:")
            second_number = input("enter second number:")
            result = float(first_number) * float(second_number)
            speak(result)

        elif "add" in result['text']:
            first_number = input("enter first number:")
            second_number = input("enter second number:")
            result = float(first_number) / float(second_number)
            speak(result)

        elif "who create you" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Recognized text: ' + result['text'])
            speak('asmit created me.')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "where are you from" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Recognized text: ' + result['text'])
            speak('i am from India')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "relaxing music" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Recognized text: ' + result['text'])
            speak(f'This is some music for you, hope you enjoy')
            os.startfile('kn.mp3')
            speak(f'What else would you like me to do, boss?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "arcade" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Recognized text: ' + result['text'])
            speak(f'This is some music for you, hope you enjoy')
            os.startfile('arcade.mp3')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            speak(f'What else would you like me to do, boss?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "note" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Recognized text: ' + result['text'])
            speak(f'This is notepad for sir to note')
            os.system('notepad')
            speak(f'What else would you like me do do, sir?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')




        elif "stop" in result or "exit" in result or "bye" in result['text']:
            speak("Assistant is off. Goodbye sir")
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load('fg.mp3')
            pygame.mixer.music.play()
            sleep(2)
            quit()

        elif "joke" in result['text']:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())
            speak(f'What else would you like me do do, sir?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "switching to text mode" in result['text']:
            print('Recognized text: ' + result['text'])
            speak(f'switching to text mode')

            from text import code
            code()


        elif "near earth objects" in result['text']:
             print('Recognized text: ' + result['text'])
             speak(f'connecting to NASA')
             try:
               from Nasa import Astro
               speak("tell me the starting date sir!")
               start = input("Enter the starting date :")
               speak("tell me the end date.")
               end = input("Enter the ending date :")
               Astro(start, end)
               Astro()
             except:
                speak("Can't connect to NASA's computer")
                print("")


        elif "google" in result['text']:
            try:
                webbrowser.open("https://www.google.com")
                speak("opening google")
                print("opening google")
            except:
                speak("Internet connection error")
                print("")

        else:
            os.system('cls')
            stream.stop_stream()
            print('Recognized text:' + result['text'])
            pass
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

asmit()








