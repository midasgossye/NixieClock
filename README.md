# RPiNixieClock

This github repo contains the software code for a Raspberry pi powered Nixie Clock. This software was written to power the 6 digit IN-12 Nixie Tube Clock based on a Raspberry Pi Zero W, but can easily be ported to cater other configurations of Nixie tubes and RPi models. The schematics, board layout and BOM files for the accompanying hardware can be found in the following repo: 


## Getting Started

These instructions will get you a copy of the project up and running on your particular Raspberry Pi:

### Prerequisites

Before you begin, make sure you have a Raspberry Pi up and running with the latest version of Raspbian (available for download here: https://www.raspberrypi.org/downloads/raspbian/). The software works on both the Lite and full Desktop versions.

Run an update and upgrade routine to make sure you have all of the latest packages installed:
```bash
sudo apt-get update
sudo apt-get upgrade
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
sudo apt-get install python-rpi.gpio
```
Next, make sure you have pip installed:
```bash
sudo apt-get install python-pip
```
Finally, use pip to install the requests module:
```bash
pip install requests
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

### Set weather location

In order to set the correct location for the weather data, 
```
Give an example
```

## Authors

* **Midas Gossye** - [Github](https://github.com/midasgossye)
* **Joshua Spaander** - 

## License

This project is licensed under the MIT License

## Acknowledgments

* This project was inspired by and partly based on the New Precise Nixie Clock from the 
* Inspiration
* etc
