#!/bin/bash
set -e

ssh -v -o StrictHostKeyChecking=no travis@206.189.200.76 << ENDSSH
  cd /home/sites/www.imtoodumbtofigureout531onmyown-staging.com/
  sudo docker stop jmeans319/531
  sudo docker rm jmeans319/531
  sudo docker image prune -a -f
  sudo git pull
  sudo docker build .
  sudo systemctl restart gunicorn-imtoodumbtofigureout531onmyown-staging.com.service
ENDSSH