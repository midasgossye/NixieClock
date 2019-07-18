# RPiNixieClock
![alt-text](https://cdn.tindiemedia.com/images/resize/VZ_aR5HRgS92k0rPrdXo-EirYys=/p/fit-in/653x435/filters:fill(fff)/i/92521/products/2019-04-29T14%3A36%3A42.298Z-IMG_4452.JPG)


This github repo contains the software code for a Raspberry pi powered Nixie Clock. This software was written to power the 6 digit IN-12 Nixie Tube Clock based on a Raspberry Pi Zero W, but can easily be ported to cater other configurations of Nixie tubes and RPi models. The schematics, board layout and BOM files for the accompanying hardware can be found in the following repo: https://github.com/midasgossye/NixieClockHardware/

Would you love to have a nixie clock at home that you can reprogram yourselves? You can buy one of my homebuilt nixie clocks with IN-12A tubes fully assembled, working and preloaded with this software from tindie: [link](https://www.tindie.com/products/midasgossye/unique-6-digit-in-12-nixie-clock-with-wifi/)


## Getting Started

These instructions will get you a copy of the project up and running on your particular Raspberry Pi:

### Prerequisites

Before you begin, make sure you have a Raspberry Pi up and running with the latest version of Raspbian (available for download here: https://www.raspberrypi.org/downloads/raspbian/). The software works on both the Lite and full Desktop versions.

Run an update and upgrade routine to make sure you have all of the latest packages installed:
```bash
sudo apt update
sudo apt upgrade
```
Because the hardware uses almost all of the GPIO pins of the RPi, including ones normally reserved for serial, I2C & SPI communication, it is necessary to disable these interfaces using the raspi-config menu:
```bash
sudo raspi-config
```
Go to submenu 5: Interfacing options, and disable the following interfaces:
```bash
SPI
I2C
Serial
1-Wire
```
![alt text](https://i.ibb.co/CVgkCnw/raspi-config.png)


In order to access the GPIO pins of the RPi, the program uses the RPi.GPIO module. Make sure you have the latest version installed:
```bash
sudo apt install python-rpi.gpio
```
Next, make sure you have pip installed:
```bash
sudo apt install python-pip
```
Use pip to install the requests module:
```bash
pip install requests
```

Finally, make sure you have git installed:
```bash
sudo apt install git
```

### Installing

The installation process is very straightforward, start by cloning the github repo:

```bash
git clone https://github.com/midasgossye/NixieClock.git
```
Navigate to the NixieClock directory:
```bash
cd NixieClock
```
Run the clock.py program:
```bash
python clock.py
```
And if everything went well, you should have a functioning Nixie Clock!


## Usage

### Set time-zone

If the clock displays the wrong time, you probably haven't adjusted the time-zone setting yet in the raspi-config menu. 
Go to raspi-config menu:
```
sudo raspi-config
```
Select option 4: localisation options

Next, select I2: Change TimeZone

Follow the wizard to change the timezone.

### Set-up weather API
In order to get the weather API functionality to work, you first need to register an account at [openweathermap](https://openweathermap.org/api). After you have signed up for a free account, you will recieve an API-key that needs to be inserted into the *clock_w_temp.py* program. You can also change the weather location by typing in your closest city name.

```python
weather_location = 'Ghent'                              # Set weather location (city)
weather_api_key = 'PUT YOUR OWN API KEY HERE'           # OpenWeather API key
```

## Authors

* **Midas Gossye** - [Github](https://github.com/midasgossye)
* **Joshua Spaander** - [Github](https://github.com/joshuaspaander)

## License

This project is licensed under the MIT License

## Acknowledgments

* This project was inspired by and partly based on the New Precise Nixie Clock from the May 2016 issue of Elektor Magazine [(link)](https://www.elektormagazine.com/magazine/elektor-201605/28960)
* IoT connectivity inspired by EEVBlog Nixie Tube Display Project [(link)](https://www.youtube.com/playlist?list=PLvOlSehNtuHutdg1kZkG7aAYhjoJnk2fc)
