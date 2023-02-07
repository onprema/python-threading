FROM python:3
WORKDIR /src
RUN apt-get update && apt-get install -y man
ADD ./requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt
ADD . /src