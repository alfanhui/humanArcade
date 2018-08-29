#!/bin/bash

sudo apt-get update && apt-get upgrade -y
sudo apt-get dist-upgrade
sudo apt-get install python-dev
sudo apt-get install python-pip
sudo pip install evdev
sudo apt-get install python-gi gir1.2-gst-plugins-base-1.0 gir1.2-gtk-2.0 gir1.2-gtk-3.0
sudo apt-get install pulseaudio pulseaudio-module-bluetooth vlc blueman
echo "Install complete, please restart"
