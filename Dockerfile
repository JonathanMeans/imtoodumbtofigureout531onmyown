FROM python:3.8
RUN mkdir /project
WORKDIR /project
COPY requirements.txt /project/
COPY requirements-dev.txt /project/
RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt
COPY . /project/
