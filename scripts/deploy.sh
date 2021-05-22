#!/bin/bash
set -e

ssh -v -o StrictHostKeyChecking=no travis@206.189.200.76 << ENDSSH
  cd /home/sites/www.imtoodumbtofigureout531onmyown-staging.com/
  sudo systemctl stop gunicorn-imtoodumbtofigureout531onmyown-staging.com.service
  sudo git pull
  sudo systemctl restart gunicorn-imtoodumbtofigureout531onmyown-staging.com.service
ENDSSH