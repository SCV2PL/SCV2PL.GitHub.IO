#!/bin/sh

python3 /home/luke_green_player/Startup_Files/clear_todaysum.py

python3 /home/luke_green_player/Startup_Files/update_todaysum.py

python3 /home/luke_green_player/Startup_Files/clear.py

python3 /home/luke_green_player/Startup_Files/update.py

python3 /home/luke_green_player/Startup_Files/selenium_datawrapper.py

# vim /etc/init.d/startupscript.sh
