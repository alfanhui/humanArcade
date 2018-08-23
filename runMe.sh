#!/bin/bash

sudo apt-get update && apt-get upgrade -y
sudo apt-get install python-dev
sudo apt-get install python-pip
sudo pip install evdev
sudo pip install bluetool 
sudo pip install playsound
sudo cp /home/pi/Desktop/source.py /etc/init.d/
echo "Install complete, please restart"
