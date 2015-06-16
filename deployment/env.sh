#!/bin/sh
. /home/{{ app_name }}/{{ app_name }}/venv/bin/activate
export DEBUG=0
export MEDIA_ROOT=/home/{{ app_name }}/media/
export STATIC_ROOT=/home/{{ app_name }}/static/
