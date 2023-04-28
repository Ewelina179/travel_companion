#!/bin/bash

python ./backend/companion/manage.py makemigrations
python ./backend/companion/manage.py migrate
python ./backend/companion/manage.py runserver 0.0.0.0:8000