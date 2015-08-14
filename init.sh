#!/bin/sh
pyvenv venv
. venv/bin/activate
pip install -r requirements.txt
./manage.py migrate
