#!/bin/bash

pip3 install psycopg2
pip3 install requests
pip3 install mysqlclient
pip3 install --no-cache-dir -r /usr/src/app/ProtoAF/requirements.txt
cd /usr/src/app/ProtoAF/ArielFrance/
./manage.py migrate --run-syncdb
./manage.py runserver 0.0.0.0:8000

/bin/bash
