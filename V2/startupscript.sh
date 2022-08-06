#! /bin/bash
# 2022-01-29 - full automation for daily updates, lines: 18, 21, 29, 37 , 36, 47, 98, 106, 111, 117, 168, 171
# python3 /home/luke_blue/Startup_Files/import_csv_data_from_urls.py
# 2022-02-11 10:27:00 UPGRADE_2.0_APP Complete
python3 /app/import_csv_data_from_urls.py
# 2022-01-30 - full automation for daily updates, lines: 22, 32
# python3 /home/luke_blue/Startup_Files/UPGRADE_2.0_APP/update_districts_j1_xy_d3_todaycount.py
# 2022-02-08 22:32:00 Evening UPGRADE_2.0_APP Complete
python3 /app/update_districts_j1_xy_d3_todaycount.py

python3 /app/clear_districts_j1_xy_d3_todaycount.py

python3 /app/autofill_districts_j1_xy_d3_todaycount.py

python3 /app/clear_districts_date_xy.py

python3 /app/update_districts_date_xy.py

python3 /app/clear_avr7d10000_todaysum_xy_support.py

python3 /app/update_avr7d10000_todaysum_xy_support.py

python3 /app/clear_avr7d_ir28_fdr21.py
# 2022-01-29 - full automation for daily updates, lines: 33, 43, 53
python3 /app/update_avr7d_ir28_fdr21.py
# 2022-01-30 - full automation for daily updates, lines: 22
# python3 /home/luke_blue/Startup_Files/update_districts_avrxypl.py
# 2022-02-08 22:32:00 Evening UPGRADE_2.0_APP Complete
python3 /app/update_districts_avrxypl.py
# 2022-01-29 - full automation for daily updates, lines: 30
#python3 /app/import_csv_data_from_url_vaccination.py
# 2022-02-06 full automation for app 
# python3 /home/luke_blue/Startup_Files/datawrapper_api_update_custom_lines.py
# 2022-02-11 10:27:00 UPGRADE_2.0_APP Complete
python3 /app/datawrapper_api_update_custom_lines.py
# python3 /home/luke_blue/Startup_Files/selenium_datawrapper.py
# 2022-02-11 10:27:00 UPGRADE_2.0_APP Complete
python3 /app/datawrapper_api_republish_set_for_epidemic_app.py

python3 /app/block_range_avr7d10000todaysumd_districtsxyf.py
# 2022-01-29 - full automation for daily updates, lines: 39, 40, 55, 56, 78, 104, 125, 152
python3 /app/save_daily_sum.py
# 2022-08-06 - full automation for update changes
python3 /app/update_Support_-_7DAVRDLR14D_t-t14_range.py
# 2022-01-29 - full automation for daily updates, lines: 19, 27, 31, 39, 43, 49, 100
# python3 /home/luke_blue/Startup_Files/correction_import_csv_data_for_voivodeships.py
# 2022-02-12 09:48:00 UPGRADE_2.0_APP Complete
python3 /app/datawrapper_api_update_external_data.py
# 2022-08-06 - full automation for update changes
python3 /app/datawrapper_api_republish_set_for_update_Support_-_7DAVRDLR14D_t-t14_range.py
# 2022-02-13 09:48:00 UPGRADE_2.0_APP Complete
# for sunday update
python3 /app/sunday_update/add_weekly_sheets_set.py
# 2022-02-13 09:48:00 UPGRADE_2.0_APP Complete
# for sunday update & cleaning
python3 /app/sunday_update/update_avr7d_array_range_7d.py
# for daily cleaning
# 2022-08-06 - full automation for update changes: loop while repeat 3 times
python3 /app/delete_unnecessary_rows_in_SUM_sheets.py
# 2022-08-06 - full automation for update changes
python3 /app/update_n+4_for_config_for_delete_unnecessary_rows_in_SUM_sheets_py.py

# /app/startupscript.sh
# chmod u+r+x
