#getting base image
FROM python:3.7

MAINTAINER maharshi chattopadhyay

ADD ./codes /

RUN pip install -r requirements.txt


