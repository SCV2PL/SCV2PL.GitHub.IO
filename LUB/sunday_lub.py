# Import the os module
import os
from github import Github
from datetime import datetime
import time
import sys
import shutil

g = Github("********************")
# or  g = github.Github(login, password)

repo = g.get_user().get_repo("scv2pl")


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


time.sleep(5)


contents1 = repo.get_contents("startupscript.sh")
with open('/home/blox_land/scv2pl/startupscript.sh', 'r') as file:
    content1 = file.read()

# update
repo.update_file(contents1.path, "Save: startupscript.sh", content1, contents1.sha)

print(content1)


contents2 = repo.get_contents("heroku_save_config_pyyaml_files_to_github.py")
with open('/home/blox_land/scv2pl/heroku_save_config_pyyaml_files_to_github.py', 'r') as file:
    content2 = file.read()

# update
repo.update_file(contents2.path, "Save: heroku_save_config_pyyaml_files_to_github.py", content2, contents2.sha)

print(content2)


time.sleep(180)


# Get directory name
mydir = ("/home/blox_land/scv2pl")

# Try to remove the tree; if it fails, throw an error using try...except.
try:
    shutil.rmtree(mydir)
except OSError as e:
    print("Error: %s - %s." % (e.filename, e.strerror))
