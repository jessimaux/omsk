# pull official base image
FROM python:3.10-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create the app user
RUN adduser -D appuser

# install psycopg2 dependencies
RUN apk update \
    && apk add python3-dev gcc libpq-dev postgresql postgresql-contrib musl-dev freetype-dev

RUN pip install -U pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .