import pyttsx3  # thư viện để nó có thể nói được những gì mình đánh vào trong code
import datetime  # thư viện để import giờ vào
import \
    speech_recognition as sr  # cái thư viện này quan trọng để có thể nhận dạng và xử lý sơ bộ giọng nói đầu vào của mình
import webbrowser as wb
import os
import playsound
import time
import requests
from playsound import playsound  # mình import cái này để nó có thể phát âm thanh
import msvcrt as m
import pygame
from time import sleep
import pyjokes

def wait():
    m.getch()


PTNK_AI_assistant = pyttsx3.init()  # khởi động text sang giọng nói ^^
voice = PTNK_AI_assistant.getProperty('voices')
assistant_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enUS_EvaM'  # đây là đường dẫn trong registry của Microsoft Windows của giọng nữ Microsoft Zira
PTNK_AI_assistant.setProperty('voice', assistant_voice_id)


def speak(audio):
    print('April: ' + audio)
    PTNK_AI_assistant.say(audio)
    PTNK_AI_assistant.runAndWait()


def time():
    Time = datetime.datetime.now().strftime(
        '%I:%M: %p')  # giải thích nè ^^: %I là giờ loại 12 tiếng, %M là phút, %p là AM hay PM
    speak('It is')
    speak(Time)


def date():
    today = datetime.datetime.now().strftime(
        'the date today is %d %m %Y, please notice that the format is day, month, year')
    speak(today)
def month():
    bh = datetime.datetime.now().strftime(
        '%m')  # giải thích nè ^^: %I là giờ loại 12 tiếng, %M là phút, %p là AM hay PM
    speak('It is')
    speak(bh)

def welcome():  # đây là mình tạo một cái function chào hỏi dựa theo thời gian mỗi khi khởi động PTNK_AI_ASSISTANT
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


internetstatus = 0
url = "https://www.google.com/"
timeout = 1.5
try:
    request = requests.get(url, timeout=timeout)
    internetstatus = 1
except (requests.ConnectionError, requests.Timeout) as exception:
    internetstatus = 2


def command():  # Đây là mình tạo một cái function nghe và xử lý giọng nói của mình theo tiếng việt
    if internetstatus == 1:
        print(' ')
        print('Listening.....')

        c = sr.Recognizer()
        with sr.Microphone() as source:
            c.pause_threshold = 1
            audio = c.listen(source)
        try:
            print('Recognizing.....')
            query = c.recognize_google(audio, language='en-US')  # en-US #vi
            print('Boss: ' + query)
        except sr.UnknownValueError:
            print('Sorry, I did\'t get that. :( Try typing the command, (tips: type 10 instead of "ten") ')
            query = str(input('your favor is: '))
        return query
    if internetstatus == 2:
        print('No internet! If your pc have connected to the internet, type: internet')
        print('Or if your pc have not connected to the internet,')
        from main import asmit

        asmit()


def asmi():  # đây là phần quan trọng nhất. Đó là phần xử lý yêu cầu của mình
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('fg.mp3')
    pygame.mixer.music.play()
    sleep(2)
    speak('successfully switch to online mode')

    welcome()  # mình đã tạo một function chào nên giờ mình chỉ cần viết welcome ra thôi ^^
    while True:
        query = command().lower()  # cái bước này là cái bước chuyển tất cả chữ viết hoa trong lời nói của mình thành chữ viết thường để máy dễ tra đúng hơn

        if "hello" in query:
            os.system('cls')
            print('Boss: ' + query)
            speak(f'Hello my boss')
            speak(f'How can I help you now boss?')
        elif "how are you" in query:
            os.system('cls')
            print('Boss: ' + query)
            speak(f'I am feeling good today. Thank you')
            speak(f'How can I help you now boss?')

        elif "switch to offline voice mode" in query:
            from main import asmit

            asmit()


        elif 'google' in query:  # ở đây mình làm theo kiểu xử lý theo từ khóa, tức là trong yêu cầu của mình chỉ cần có từ khóa đó là nó sẽ thực thi, tương tự với mấy cái phía dưới
            os.system('cls')
            print('Boss: ' + query)
            speak('What should I search now boss?')
            search = command().lower()
            url = f'https://www.google.com/search?q={search}'
            wb.get().open(url)
            speak(f'I found something on Google for your search:')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')


        elif 'weather' in query:
            os.system('cls')
            print('Boss: ' + query)
            url = f'https://www.google.com/search?q=weather'
            wb.get().open(url)
            speak(f'This is your local weather!')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')

            speak(f'what else you would like me to do, boss?')


        elif "youtube" in query:
            os.system('cls')
            print('Boss: ' + query)
            speak('What should I search on youtube now boss?')
            search = command().lower()
            url = f'https://youtube.com/search?q={search}'
            wb.get().open(url)
            speak(f'I found something on Youtube for your search:')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            
            speak(f'what else you would like me to do, boss?')

        elif "quit" in query:
            os.system('cls')
            print('Boss: ' + query)
            speak("Assistant is off. Goodbye boss")
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load('fg.mp3')
            pygame.mixer.music.play()
            sleep(2)
            quit()


        elif 'time' in query:
            os.system('cls')
            print('Boss: ' + query)
            time()
            speak(f'what else you would like me to do, boss?')
        elif 'date' in query:
            os.system('cls')
            print('Boss: ' + query)
            date()
            speak(f'what else you would like me to do, boss?')
        elif 'month' in query:
            os.system('cls')
            print('Boss: ' + query)
            month()
            speak(f'what else you would like me to do, boss?')


        elif 'you can' in query:  # làm, chức năng,
            os.system('cls')
            print('Boss: ' + query)
            speak('I can tell you the time and weather.')
            speak('I also can open browser or youtube.')
            speak('In addition, I can open some review tests for your grade.')
            speak('Besides, I can open a typing test with many languages supported')
            speak('I can open translator, google maps and google earth too!')
            speak('So, what would you like me to do now boss?')

        elif 'joke' in  query:
           a1= speak(pyjokes.get_joke())
           print(a1)
        elif '  who create you' in query:  # làm, chức năng,
            os.system('cls')
            print('Boss: ' + query)
            speak("Asmit  Dutta made me")

        else:
            pass


if __name__ == '__main__':
    asmi()  # nguyên một dãy code phía trên mình đã define 'thực_thi_trợ_lý_ảo_STEAM_PTNK nên giờ chỉ cần gọi nó ra ^^, để dấu () ở cuối để nó làm thành vòng lặp