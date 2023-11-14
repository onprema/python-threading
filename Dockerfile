FROM python:3.12
WORKDIR /src
RUN apt-get update && apt-get install -y man htop imagemagick
ADD ./requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt
ADD . /src