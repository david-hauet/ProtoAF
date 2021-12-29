#!/bin/bash
set echo on

echo "Installing mysqlclient..."
pip3 install mysqlclient
echo "Installing psycopg2..."
pip3 install psycopg2
echo "Installing requests..."
pip3 install requests
echo "Installing requirements..."
pip3 install --no-cache-dir -r /usr/src/app/ProtoAF/requirements.txt
cd /usr/src/app/ProtoAF/ArielFrance/
echo "Migrate DB..."
./manage.py migrate --run-syncdb
export DJANGO_SUPERUSER_PASSWORD=admin
export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_EMAIL=admin@arielfrance.com
echo "Create SuperUser..."
./manage.py createsuperuser --noinput
echo "Finally RunServer !!! ..."
./manage.py runserver 0.0.0.0:8000

/bin/bash
