FROM python:buster

RUN apt-get update
RUN apt-get install python3 python3-pip libgeos-div libgdal-lib proj-bin spatialite-bin
