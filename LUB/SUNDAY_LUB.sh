#! /bin/bash
python3 /home/blox_land/LUB/lub.py

heroku git:clone -a scv2pl

cd scv2pl

python3 /home/blox_land/LUB/sunday_lub.py

git status

git add .

git commit -am "PUSH"

git push heroku main

git update-index --chmod=+x startupscript.sh

git ls-files --stage

git status

git restore .

git commit -am "startupscript.sh ==> 100755 mode"

git push heroku main
