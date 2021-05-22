#!/bin/bash
set -e
SITE_NAME=$1

ssh -v -o StrictHostKeyChecking=no travis@206.189.200.76 << ENDSSH
  cd /home/sites/www.${SITE_NAME}/
  sudo systemctl stop gunicorn-${SITE_NAME}.service
  sudo git reset --hard HEAD
  sudo git pull
  sudo env/bin/python manage.py collectstatic --no-input
  sudo systemctl restart gunicorn-${SITE_NAME}.service
ENDSSH