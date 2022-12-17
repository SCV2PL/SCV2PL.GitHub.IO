#! /bin/bash

cd LUB

source LUB/bin/activate

python3 /home/blox_land/LUB/sunday_lub.py

cd ..

heroku git:clone -a scv2pl

cd scv2pl

git update-index --chmod=+x startupscript.sh

git ls-files --stage

git status

git restore .

git commit -am "startupscript.sh ==> 100755 mode"

git push heroku main
