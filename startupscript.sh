#!/bin/sh

python3 /home/luke_blue/Startup_Files/update_districts_j1_xy_d3_todaycount.py

python3 /home/luke_blue/Startup_Files/clear_districts_j1_xy_d3_todaycount.py

python3 /home/luke_blue/Startup_Files/autofill_districts_j1_xy_d3_todaycount.py

python3 /home/luke_blue/Startup_Files/clear_districts_date_xy.py

python3 /home/luke_blue/Startup_Files/update_districts_date_xy.py

python3 /home/luke_blue/Startup_Files/clear_avr7d10000_todaysum_xy_support.py

python3 /home/luke_blue/Startup_Files/update_avr7d10000_todaysum_xy_support.py

python3 /home/luke_blue/Startup_Files/clear_avr7d_ir28_fdr21.py

python3 /home/luke_blue/Startup_Files/update_avr7d_ir28_fdr21.py

python3 /home/luke_blue/Startup_Files/daily_update/update_districts_avrxypl.py

python3 /home/luke_blue/Startup_Files/selenium_datawrapper.py

# vim /etc/init.d/startupscript.sh
