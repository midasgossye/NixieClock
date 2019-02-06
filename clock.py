# -*- coding: utf-8 -*-
"""
Created on Sat May 19 13:40:46 2018
@author: midas
"""
import RPi.GPIO as GPIO
import time
import requests
import json

weather_api_key = '526537c20da268624d9eab82a24f4ceb'

Nixie_pinout = [[12, 16, 18, 22],
                [24, 26, 32, 36],
                [38, 40, 37, 35],
                [33, 31, 29, 23],
                [21, 19, 15, 13],
                [11, 7, 5, 3]]
Neon_pins = [10,8]


def init_GPIO(Nixie_pinout, Neon_pins):
    GPIO.setmode(GPIO.BOARD)
    for Nixie_pins in Nixie_pinout:
        GPIO.setup(Nixie_pins, GPIO.OUT)
    GPIO.setup(Neon_pins, GPIO.OUT)

    
def display_number(Number, Nixie_pinout):
    num_str = str(Number)
    while len(num_str) < 6:
        num_str = '0' + num_str
    i = 0
    for digit in num_str:
        num_digit = int(digit)
        binary = '{0:04b}'.format(num_digit)
        binary = map(int, binary)
        GPIO.output(Nixie_pinout[i], binary)
        i += 1
        

init_GPIO(Nixie_pinout, Neon_pins)
Neon = True
count = 0
prev_time = "0"
while(1):
    loc_time = time.strftime("%H%M%S")
    if loc_time != prev_time:
        count += 1
        display_number(int(loc_time), Nixie_pinout)
        if Neon:
            GPIO.output(Neon_pins, [0,0])
            Neon = False
        else:
            GPIO.output(Neon_pins, [1,1])
            Neon = True
        prev_time = loc_time
    if count > 30:
        count = 0
        GPIO.output(Neon_pins, [1,0])
        Neon = False
        r = requests.get("http://api.openweathermap.org/data/2.5/weather", params = {'q' : 'Wetteren', 'appid' : weather_api_key})
        weather_data = json.loads(r.text)
        display_number(int(weather_data[u'main'][u'temp'])-273, Nixie_pinout)
        time.sleep(5)
    time.sleep(0.1)

GPIO.cleanup()
