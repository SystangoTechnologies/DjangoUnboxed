#!/bin/sh
python manage.py migrate
while true
do
    python manage.py runserver_plus 0.0.0.0:8000
done
