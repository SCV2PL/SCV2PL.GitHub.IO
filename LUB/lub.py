import os
import sys
import shutil

# Get directory name
mydir = ("/home/blox_land/scv2pl")

# Try to remove the tree; if it fails, throw an error using try...except.
try:
    shutil.rmtree(mydir)
except OSError as e:
    print("Error: %s - %s." % (e.filename, e.strerror))
