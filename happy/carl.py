import requests
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import os
from PIL import Image
import random
import pyttsx3
import msvcrt as m

APRIL = pyttsx3.init('sapi5')
voice = APRIL.getProperty('voices')
assistant_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enUS_ZiraM'
rate = APRIL.getProperty('rate')
APRIL.setProperty('rate', 170)
voices = APRIL.getProperty('voices')
APRIL.setProperty('voice', assistant_voice_id)


def speak(audio):
    APRIL.say(audio)
    APRIL.runAndWait()


Api_Key = "bRwpUuFWhuTpcQrutjrigQDsTi4GQhBBJIsLAnJR"



def astro(start_date,end_date):

    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={Api_Key}"

    r = requests.get(url)

    Data = r.json()

    Total_Astro = Data['element_count']

    neo = Data['near_earth_objects']
    speak(f"Total Astroid Between {start_date} and {end_date} Is : {Total_Astro}")
    speak("Extact Data For Those Astroids Are Listed Below ")

    for body in neo[start_date]:

        id = body['id']

        name = body['name']

        absolute = body['absolute_magnitude_h']

        print(id,name,absolute)

def issTracker():
    url = "http://api.open-notify.org/iss-now.json"

    r = requests.get(url)

    Data = r.json()

    dt = Data['timestamp']

    lat = Data['iss_position']['latitude']

    lon = Data['iss_position']['longitude']

    print(f"Time And Date : {dt}")
    print(f"Latitude : {lat}")
    print(f"Longitude : {lon}")
    speak(f"Time And Date : {dt}")
    speak(f"Latitude : {lat}")
    speak(f"Longitude : {lon}")
