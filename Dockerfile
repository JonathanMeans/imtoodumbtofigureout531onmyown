FROM python:3.8
SHELL ["/bin/bash", "-c"]

# create the app user
ENV HOME=/home/sites
ENV APP_HOME=/home/sites/www.imtoodumbtofigureout531onmyown.com
RUN mkdir $HOME
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
WORKDIR $APP_HOME

# install psycopg2 dependencies
# RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN apt-get update && apt-get install -y netcat

COPY requirements.txt $APP_HOME
COPY requirements-dev.txt $APP_HOME
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt
COPY . $APP_HOME

ENTRYPOINT ["./entrypoint.sh"]