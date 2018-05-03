#!/bin/sh
#python /app/manage.py collectstatic --noinput --clear
python /app/manage.py migrate
uwsgi --ini /production.ini

