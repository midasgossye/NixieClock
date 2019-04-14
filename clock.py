# -*- coding: utf-8 -*-
"""
Created on Sat May 19 13:40:46 2018
@author: midas
"""
from NixieDriver import Nixie
import time
import requests
import json
from random import randint

weather_api_key = '526537c20da268624d9eab82a24f4ceb'


Nixie_disp = Nixie()


count = 0
count2 = 0
avoid_poisoning_interval = randint(60, 120)
prev_time = "0"
while(1):
    loc_time = time.strftime("%H%M%S")
    if loc_time != prev_time:
        count += 1
        count2 += 1
        Nixie_disp.display_number(int(loc_time))
        Nixie_disp.toggleNeon()
        prev_time = loc_time
    if count > 30:
        count = 0
        r = requests.get("http://api.openweathermap.org/data/2.5/weather", params = {'q' : 'Aberdeen', 'appid' : weather_api_key})
        weather_data = json.loads(r.text)
        temp = int(round(weather_data[u'main'][u'temp'])-273.15)
        if temp < 0:
            Nixie_disp.setNeon([0, 1])
        else:
            Nixie_disp.setNeon([0, 0])
        Nixie_disp.display_number(abs(temp), leading_zeros=False)
        time.sleep(5)
    if count2 > avoid_poisoning_interval:
        for i in range(0, 10*111111, 111111):
            Nixie_disp.display_number(i)
            time.sleep(0.5)
        count2 = 0
        avoid_poisoning_interval = randint(600, 1200)
    time.sleep(0.1)

GPIO.cleanup()
