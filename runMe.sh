#!/bin/bash

sudo apt-get update && apt-get upgrade -y
sudo apt-get install python-dev
sudo apt-get install python-pip
sudo pip install evdev
sudo pip install bluetool 
sudo pip install playsound
sudo apt-get install python-gi gir1.2-gst-plugins-base-1.0 gir1.2-gtk-2.0 gir1.2-gtk-3.0
sudo cp /home/pi/Desktop/source.py /etc/init.d/
echo "Install complete, please restart"
