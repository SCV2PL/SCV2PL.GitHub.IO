#!/bin/sh
# daily update line 13, 16, 24, 32 , 36, 42, 92, 101, 106, 112, 163, 166
python3 /home/luke_blue/Startup_Files/import_csv_data_from_urls.py
# daily update line 22, 32
python3 /home/luke_blue/Startup_Files/update_districts_j1_xy_d3_todaycount.py

python3 /home/luke_blue/Startup_Files/clear_districts_j1_xy_d3_todaycount.py

python3 /home/luke_blue/Startup_Files/autofill_districts_j1_xy_d3_todaycount.py

python3 /home/luke_blue/Startup_Files/clear_districts_date_xy.py
# daily update line 22
python3 /home/luke_blue/Startup_Files/update_districts_date_xy.py

python3 /home/luke_blue/Startup_Files/clear_avr7d10000_todaysum_xy_support.py

python3 /home/luke_blue/Startup_Files/update_avr7d10000_todaysum_xy_support.py

python3 /home/luke_blue/Startup_Files/clear_avr7d_ir28_fdr21.py
# daily update line 22, 32, 42
python3 /home/luke_blue/Startup_Files/update_avr7d_ir28_fdr21.py
# daily update line 22
python3 /home/luke_blue/Startup_Files/daily_update/update_districts_avrxypl.py

python3 /home/luke_blue/Startup_Files/selenium_datawrapper.py

python3 /home/luke_blue/Startup_Files/block_range_avr7d10000todaysumd_districtsxyf.py
# daily update line 25,26, 41, 42, 64, 89
python3 /home/luke_blue/Startup_Files/save_daily_sum.py

# vim /etc/init.d/startupscript.sh
