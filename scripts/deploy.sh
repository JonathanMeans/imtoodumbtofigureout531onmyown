#!/bin/bash
set -e

ssh -v -o StrictHostKeyChecking=no travis@206.189.200.76 << ENDSSH
  cd /home/sites/www.imtoodumbtofigureout531onmyown-staging.com/
  docker stop jmeans319/531
  docker rm jmeans319/531
  docker image prune -a -f
  docker pull jmeans319/531
  git pull
  sudo systemctl restart gunicorn-imtoodumbtofigureout531onmyown-staging.com.service
ENDSSH