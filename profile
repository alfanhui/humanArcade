# /etc/profile: system-wide .profile file for the Bourne shell (sh(1))
# and Bourne compatible shells (bash(1), ksh(1), ash(1), ...).

if [ "`id -u`" -eq 0 ]; then
  PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
else
  PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games"
fi
export PATH

if [ "${PS1-}" ]; then
  if [ "${BASH-}" ] && [ "$BASH" != "/bin/sh" ]; then
    # The file bash.bashrc already sets the default PS1.
    # PS1='\h:\w\$ '
    if [ -f /etc/bash.bashrc ]; then
      . /etc/bash.bashrc
    fi
  else
    if [ "`id -u`" -eq 0 ]; then
      PS1='# '
    else
      PS1='$ '
    fi
  fi
fi

if [ -d /etc/profile.d ]; then
  for i in /etc/profile.d/*.sh; do
    if [ -r $i ]; then
      . $i
    fi
  done
  unset i
fi
echo "**************************** RASPBERRY AND SCARLETT PI *******************"
echo "* Human Arcade program has been set to open upon boot.                   *"
echo "* To get the desktop back, run: sudo raspi-config                        *"
echo "* Select “Boot Options” then change “Desktop/CLI” to “Desktop Autologin” *"
echo "* To stop the program from autoloading,                                  *"
echo "*'sudo nano /etc/profile' and remove last line.                          *"
echo "**************************************************************************"

echo "Starting Pulse audio"
sleep 1
pulseaudio --start
echo -e 'power on \n\nconnect 00:11:67:13:52:E6 \n\nquit' | bluetoothctl
sleep 3
pacmd set-default-sink bluez_sink.00_11_67_13_52_E6.headset_head_unit
echo -e 'power on \n\npair 00:1F:E2:9A:A3:45 \n\ntrust 00:1F:E2:9A:A3:45 \n\nconnect 00:1F:E2:9A:A3:45 \n\nquit' | bluetoothctl
#this is the last line!!
python3 /home/pi/Desktop/source.py &
