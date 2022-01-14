FROM python:3.9.5-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install netcat gcc postgresql \
    && apt-get clean

COPY Pipfile* ./

RUN pip3 install -q --no-cache-dir \
    pipenv==2022.1.8 && \ 
    pipenv install --system --dev

COPY . .
COPY ./entrypoint.sh .

RUN chmod +x /usr/src/app/entrypoint.sh