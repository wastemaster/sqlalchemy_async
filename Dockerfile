FROM python:3.9.4-slim-buster

LABEL maintainer="wastemaster@gmail.com"
LABEL vendor="Morozware"

ENV \
  # python
  PYTHONFAULTHANDLER=1 \
  # Seems to speed things up
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  # Turns off writing .pyc files; superfluous on an ephemeral container.
  PYTHONDONTWRITEBYTECODE=1 \
  # pip:
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

# Install dependencies
RUN apt-get update && apt-get install -y \
   gcc \
   && rm -rf /var/lib/apt/lists/*

RUN mkdir /app
WORKDIR /app/src

COPY  . /app/src

RUN pip3 install -r /app/src/requirements.txt \
    && rm -rf /root/.cache/pip

CMD gunicorn app.server:app -b 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker --timeout 60
