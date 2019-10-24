# -*- coding: utf-8 -*-
"""
Standard Nixie Clock program
Description: Displays the current local time
Created on Sat May 19 13:40:46 2018
@author: midas
"""
from NixieDriver import Nixie
import time
from random import randint

avoid_poisoning_interval = 1800 # Set cathode poisoning prevention routine interval


Nixie_disp = Nixie() # Initialize nixie display

count_poison = 0

prev_time = "0"
while(1):
    loc_time = time.strftime("%H%M%S")              # Format local time to hhmmss
    if loc_time != prev_time:                       # If the local time needs to be updated ...
        count_poison += 1                           # Increase seconds counter for avoiding cathode poisoning routine
        Nixie_disp.display_number(int(loc_time))    # Display local time on nixies
        Nixie_disp.toggleNeon()                     # Toggle Neon indicators
        prev_time = loc_time                        # Put set local time as previous set time

   
    if loc_time[2:] == "3000" or loc_time[2:] == "0000" :     # If cathode poisoning counter reached cathode poisining prevention interval...
        for i in range(0, 10*111111, 111111):       # Loop through all digits
            Nixie_disp.display_number(i)
            time.sleep(0.5)
        count_poison = 0
    time.sleep(0.1)

GPIO.cleanup()
