#!/bin/sh
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
./manage.py migrate

npm install
gulp
