#!/usr/bin/python
# /etc/init.d/source.py
# BEGIN INIT INFO
# Provides:          source.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start daemon at boot time
# Description:       Enable service provided by daemon.
# END INIT INFO

# Co-Authored Scarlett & Stu, 2018
import pygame
from evdev import InputDevice, categorize, ecodes
import time
#from bluetool import Bluetooth
#from playsound import playsound
#import vlc

controllerMac = "00:1F:E2:9A:A3:45"
audioMac = "00:11:67:13:52:E6"

btn_x = 304
btn_o = 305
btn_t = 307
btn_s = 308

forwards = "/home/pi/Desktop/Forwards.mp3"
backwards = "/home/pi/Desktop/Backwards.mp3"
left = "/home/pi/Desktop/Left.mp3"
right = "/home/pi/Desktop/Right.mp3"
start = "/home/pi/Desktop/Start.mp3"
jump = "/home/pi/Desktop/Jump.mp3"
duck = "/home/pi/Desktop/Duck.mp3"
gameOn = "/home/pi/Desktop/GameOn.mp3"
turnControllerOn = "/home/pi/Desktop/TurnControllerOn.mp3"


def main():
    pygame.mixer.init()
    gamepad = get_controller_stream()
    interpret_buttons(gamepad)

# playsound
# def play_sound(path):
#    try:
#        playsound("/home/pi/Desktop/birds.wav")
#    except Exception as err:
#        print(err," Audio issue with %s.mp3"%path)

# vlc
# def play_sound(vlcFile):
#	try:
#		player = instance.media_player_new()
#		media = instance.media_new(vlcFile)
#		media.get_mrl()
#		player.set_media(media)
#		player.play()
#	except Exception as err:
#		print(err, " Audio issue with %s"%vlcFile)

# pygame


def play_sound(path):
    try:
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
    except Exception as err:
        print(err, " Audio issue:%s" % path)


def get_controller_stream():
    for x in range(4):
        try:
            gamepad = InputDevice("/dev/input/event" + str(x))
            if gamepad.name == "Wireless Controller":
                print("Gamepad found")
                return gamepad
        except:
            continue
    print("Turn the Controller On")
    play_sound(turnControllerOn)
    time.sleep(5)
# pair_bluetooth(controllerMac)
    return get_controller_stream()


def interpret_buttons(gamepad):
    play_sound(gameOn)
    time.sleep(3)
    print("Ready!")
    for event in gamepad.read_loop():
        check_dpad(event)
        check_buttons(event)


def check_dpad(event):
    # EV_ABS
    if event.type == ecodes.EV_ABS:
        if ecodes.ABS[event.code] == 'ABS_HAT0Y':
            if event.value == -1:
                print("up")
                play_sound(backwards)
            elif event.value == 1:
                print("down")
                play_sound(forwards)
        elif ecodes.ABS[event.code] == 'ABS_HAT0X':
            if event.value == -1:
                print("left")
                play_sound(right)
            elif event.value == 1:
                print("right")
                play_sound(left)


def check_buttons(event):
    # EV_KEY
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == btn_x:
                print("x")
                play_sound(start)
            elif event.code == btn_o:
                print("o")
                play_sound(duck)
            elif event.code == btn_t:
                print("t")
            elif event.code == btn_s:
                print("s")
                play_sound(jump)


if __name__ == "__main__":
    print("Start")
    main()
    print("Program terminated")
