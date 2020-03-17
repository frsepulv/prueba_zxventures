FROM ubuntu:latest
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get -y install python3 python3-pip libgeos-dev libgdal-dev proj-bin spatialite-bin libsqlite3-mod-spatialite
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code
RUN pip3 install -r requirements.txt
COPY . /code/

RUN [ "python3", "-m", "manage", "makemigrations" ]
RUN [ "python3", "-m", "manage", "migrate" ]

ENTRYPOINT [ "python3", "-m", "manage", "runserver" ]