FROM ubuntu:bionic
SHELL ["/bin/bash", "-c"]

RUN apt-get update && apt-get install -y \
    fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 \
    libnspr4 libnss3 lsb-release xdg-utils libxss1 libdbus-glib-1-2 \
    curl unzip wget software-properties-common \
    xvfb python3-pip

RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt-get install -y python3.8 python3.8-dev
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3.8 get-pip.py

RUN GECKODRIVER_VERSION=`curl https://github.com/mozilla/geckodriver/releases/latest | grep -Po 'v[0-9]+.[0-9]+.[0-9]+'` && \
    wget https://github.com/mozilla/geckodriver/releases/download/$GECKODRIVER_VERSION/geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz && \
    tar -zxf geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz -C /usr/local/bin && \
    chmod 777 /usr/local/bin/geckodriver && \
    rm geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz

RUN FIREFOX_SETUP=firefox-setup.tar.bz2 && \
    apt-get purge firefox && \
    wget -O $FIREFOX_SETUP "https://download.mozilla.org/?product=firefox-latest&os=linux64" && \
    tar xjf $FIREFOX_SETUP -C /opt/ && \
    ln -s /opt/firefox/firefox /usr/bin/firefox && \
    rm $FIREFOX_SETUP

# create the app user
ENV HOME=/home/sites
ENV APP_HOME=/home/sites/www.imtoodumbtofigureout531onmyown-staging.com
RUN mkdir $HOME
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
WORKDIR $APP_HOME

COPY requirements.txt $APP_HOME
COPY requirements-dev.txt $APP_HOME
RUN python3.8 -m pip install -r requirements.txt
RUN python3.8 -m pip install -r requirements-dev.txt
COPY . $APP_HOME
RUN . .env
RUN python3.8 manage.py collectstatic --no-input
#CMD gunicorn lifting.wsgi:application --bind 0.0.0.0:8080