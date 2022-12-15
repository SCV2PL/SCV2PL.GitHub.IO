# Import the os module
import os

# Set the old and new file names
old_file_name = "/home/blox_land/scv2pl/startupscript.sh"
new_file_name = "/home/blox_land/scv2pl/saturday_startupscript.sh"

# Use the os.rename() method to rename the file
os.rename(old_file_name, new_file_name)


old_file_name = "/home/blox_land/scv2pl/sunday_startupscript.sh"
new_file_name = "/home/blox_land/scv2pl/startupscript.sh"

os.rename(old_file_name, new_file_name)


old_file_name = "/home/blox_land/scv2pl/heroku_save_config_pyyaml_files_to_github.py"
new_file_name = "/home/blox_land/scv2pl/saturday_heroku_save_config_pyyaml_files_to_github.py"

os.rename(old_file_name, new_file_name)


old_file_name = "/home/blox_land/scv2pl/sunday_heroku_save_config_pyyaml_files_to_github.py"
new_file_name = "/home/blox_land/scv2pl/heroku_save_config_pyyaml_files_to_github.py"

os.rename(old_file_name, new_file_name)




