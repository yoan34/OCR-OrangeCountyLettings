FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt


CMD python manage.py runserver 0.0.0.0:8000