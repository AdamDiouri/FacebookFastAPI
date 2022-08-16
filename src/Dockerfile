FROM ubuntu:22.04

WORKDIR /usr/

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY . /usr/

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update \
    && apt-get -y install postgresql postgresql-contrib python3 python3-pip libsm6 libxext6 libxrender-dev mlocate \
    && updatedb \
    && pip install --upgrade pip setuptools wheel \
    && pip install fastapi uvicorn facebook-scraper pytest requests asyncpg databases psycopg2-binary SQLAlchemy

# ENTRYPOINT [ "python3" ,"/usr/app/api/startup.py" ]

CMD [ "uvicorn", "app.main:app", "--reload", "--workers", "1", "--host", "0.0.0.0", "--port", "8000" ]