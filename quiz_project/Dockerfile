# Base Image
FROM python:3.8

# create and set working directory
RUN mkdir /app
WORKDIR /app

# Add current directory code to working directory
ADD . /app/

# set default environment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

ENV PORT=8000

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8888
CMD waitress-serve --listen=*:$PORT quiz.wsgi:application
