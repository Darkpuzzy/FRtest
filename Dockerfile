FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update

RUN mkdir app
WORKDIR /app
RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install -r requirements.txt
