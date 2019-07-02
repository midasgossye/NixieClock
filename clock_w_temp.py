# -*- coding: utf-8 -*-
"""
Standard Nixie Clock program

Description: Displays the current local time and temperature from the openweatherAPI


Modified on Tue July 2 14:23:46 2019
@author: midas
"""
from NixieDriver import Nixie
import time
import requests
import json
from random import randint

temperature_interval = 30                               # Set temperature display interval (in secs)
weather_location = 'Ghent'                              # Set weather location (city)
weather_api_key = 'PUT YOUR OWN API KEY HERE'           # OpenWeather API key


# Use the openweathermap API to get the local temperature in deg C
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
    loc_time = time.strftime("%H%M%S")              # Format local time to hhmmss
    if loc_time != prev_time:                       # If the local time needs to be updated ...
        count_temp += 1                             # Increase seconds counter for temperature interval
        count_poison += 1                           # Increase seconds counter for avoiding cathode poisoning routine
        Nixie_disp.display_number(int(loc_time))    # Display local time on nixies
        Nixie_disp.toggleNeon()                     # Toggle Neon indicators
        prev_time = loc_time                        # Put set local time as previous set time

    if count_temp > temperature_interval:           # If temp counter reached temperature display interval...
        count_temp = 0                              # Set temperature update counter to 0
        temp = get_local_temp(weather_location, weather_api_key) # Get local temperature in degrees C
        if temp != -1000:                           # If response is valid:
            if temp < 0:                            # Show neon indicator as minus sign if temperature is negative
                Nixie_disp.setNeon([0, 1]) 
            else:
                Nixie_disp.setNeon([0, 0])
            Nixie_disp.display_number(abs(temp), leading_zeros=False) # Display (absolute) temperature on nixie tubes
            time.sleep(5)                                             # Wait 5 secs
    if count_poison > avoid_poisoning_interval: # If cathode poisoning counter reached cathode poisining prevention interval...
        for i in range(0, 10*111111, 111111): # Loop through all digits
            Nixie_disp.display_number(i)
            time.sleep(0.5)
        count_poison = 0
        avoid_poisoning_interval = randint(600, 1200)
    time.sleep(0.1)

GPIO.cleanup()
