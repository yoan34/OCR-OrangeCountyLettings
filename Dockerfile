FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get -y update

WORKDIR /app

COPY requirements.txt /app/

ARG SENTRY_DSN
ENV SENTRY_DSN $SENTRY_DSN

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . /app/

CMD python manage.py runserver 0.0.0.0:$PORT