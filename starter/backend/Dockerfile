FROM public.ecr.aws/docker/library/python:3.10-slim

ENV FLASK_RUN_HOST=0.0.0.0

WORKDIR /

RUN adduser --disabled-password --gecos "" --uid 1000 app

RUN apt-get update && \
    apt-get install -y \
    build-essential \
    gcc \
    libpcre2-dev \
    libssl-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pip install pipenv

RUN mkdir -p /var/www/app && mkdir /app

COPY Pipfile* /app/

RUN cd /app && pipenv install --system --deploy

COPY . /app

WORKDIR /app

EXPOSE 5000
CMD ["uwsgi", "--http", "0.0.0.0:5000", "--wsgi-file", "app.py", "--callable", "app"]