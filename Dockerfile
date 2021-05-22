FROM python:3.8
SHELL ["/bin/bash", "-c"]

# create the app user
ENV HOME=/home/sites
ENV APP_HOME=/home/sites/www.imtoodumbtofigureout531onmyown-staging.com
RUN mkdir $HOME
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
WORKDIR $APP_HOME

COPY requirements.txt $APP_HOME
COPY requirements-dev.txt $APP_HOME
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt
COPY . $APP_HOME
RUN python3.8 manage.py collectstatic --no-input