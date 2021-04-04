#!/bin/sh
export DJANGO_SETTINGS=prod
touch /app/log/kamenica.log
touch /app/log/uwsgi.log
cd /app
python3 manage.py migrate

if [ "$#" -ne 0 ]; then
  echo "python3 manage.py" "$@"
  python3 manage.py "$@"
else
  uwsgi --ini /app/config/uwsgi-prod.ini
fi
