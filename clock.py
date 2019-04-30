# -*- coding: utf-8 -*-
"""
Standard Nixie Clock program

Description: Displays the current local time and temperature from the openweatherAPI


Created on Sat May 19 13:40:46 2018
@author: midas
"""
from NixieDriver import Nixie
import time
import requests
import json
from random import randint

temperature_interval = 30                               # Set temperature display interval (in secs)
weather_location = 'Wetteren'                           # Set weather location (city)
weather_api_key = '526537c20da268624d9eab82a24f4ceb'    # OpenWeather API key



def get_local_temp(weather_location, weather_api_key):
    try:
        r = requests.get("http://api.openweathermap.org/data/2.5/weather", params = {'q' : weather_location, 'appid' : weather_api_key}, timeout=0.1)
        weather_data = json.loads(r.text)
        temp = int(round(weather_data[u'main'][u'temp'])-273.15)
    except:
        return -1000

    return temp

Nixie_disp = Nixie() # Initialize nixie display


count_temp = 0
count_poison = 0
avoid_poisoning_interval = randint(60, 120)
prev_time = "0"
while(1):
    loc_time = time.strftime("%H%M%S")
    if loc_time != prev_time:
        count_temp += 1
        count_poison += 1
        Nixie_disp.display_number(int(loc_time))
        Nixie_disp.toggleNeon()
        prev_time = loc_time
    if count_temp > temperature_interval:
        count_temp = 0
        temp = get_local_temp(weather_location, weather_api_key)
        if temp != -1000:
            if temp < 0:
                Nixie_disp.setNeon([0, 1])
            else:
                Nixie_disp.setNeon([0, 0])
            Nixie_disp.display_number(abs(temp), leading_zeros=False)
            time.sleep(5)
    if count_poison > avoid_poisoning_interval:
        for i in range(0, 10*111111, 111111):
            Nixie_disp.display_number(i)
            time.sleep(0.5)
        count_poison = 0
        avoid_poisoning_interval = randint(600, 1200)
    time.sleep(0.1)

GPIO.cleanup()
