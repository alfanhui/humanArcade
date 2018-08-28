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

from evdev import InputDevice, categorize, ecodes
from bluetool import Bluetooth
from playsound import playsound

controllerMac = "00:1F:E2:9A:A3:45"  # scarletts
audioMac = "00:11:67:13:52:E6"  # scarletts

# controllerMac = "DC:0C:2D:17:8B:69" #stus
# audioMac = "" #stus

btn_x = 304
btn_o = 305
btn_t = 307
btn_s = 308


def main():
    # pair_bluetooth(audioMac)
    # pair_bluetooth(controllerMac)
    play_sound('SoundTest')
    gamepad = get_controller_stream()
    interpret_buttons(gamepad)
    # unpair_bluetooth(audioMac)
    # unpair_bluetooth(controllerMac)


def play_sound(path):
    try:
        playsound("/home/pi/Desktop/%s.mp3" % path)
    except Exception as err:
        print(err, " Audio issue with %s" % path)


def pair_bluetooth(mac):
    print("Trying to pair bluetooth device...")
    if mac == controllerMac:
        play_sound("PairingController")
    elif mac == audioMac:
        play_sound("PairingAudio")
    bluetooth = Bluetooth()
    unpair_bluetooth(mac)
    bluetooth.remove(mac)
    if bluetooth.pair(mac):
        play_sound("Paired")
    else:
        play_sound("UnableToPair")
    bluetooth.trust(mac)
    if not bluetooth.connect(mac):
        pair_bluetooth(mac)


def unpair_bluetooth(mac):
    bluetooth = Bluetooth()
    play_sound("BluetoothDisconnecting")
    bluetooth.disconnect(mac)


def get_controller_stream():
    for x in range(4):
        try:
            gamepad = InputDevice("/dev/input/event" + str(x))
            if gamepad.name == "Wireless Controller":
                print("Gamepad found")
                return gamepad
        except:
            print("Found but throwing away " + gamepad.name)
    print("Unable to connect to Controller, trying to repair device")
    play_sound("TurnControllerOn")
    pair_bluetooth(controllerMac)
    return get_controller_stream()


def interpret_buttons(gamepad):
    play_sound("Ready!")
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
                play_sound("Forward")
            elif event.value == 1:
                print("down")
                play_sound("Backward")
        elif ecodes.ABS[event.code] == 'ABS_HAT0X':
            if event.value == -1:
                print("right")
                play_sound("Left")
            elif event.value == 1:
                print("left")
                play_sound("Right")


def check_buttons(event):
    # EV_KEY
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == btn_x:
                print("x")
                play_sound("Start")
            elif event.code == btn_o:
                print("o")
                play_sound("Duck")
            elif event.code == btn_t:
                print("t")
            elif event.code == btn_s:
                print("s")
                play_sound("Jump")


if __name__ == "__main__":
    print("Start")
    main()
    print("Program terminated")
