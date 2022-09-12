
# This Dockerfile was generated by Skelebot
# Editing this file manually is not advised as all changes will be overwritten by Skelebot

FROM skelebot/python-base:3.8
MAINTAINER Sean Shookman <sms112788@gmail.com>
WORKDIR /app
RUN ["pip", "install", "setuptools"]
RUN ["pip", "install", "bcrypt~=4.0"]
RUN ["pip", "install", "sqlalchemy~=1.4"]
COPY . /app
