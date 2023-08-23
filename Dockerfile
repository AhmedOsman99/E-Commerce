FROM python:3.10.2

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY requirements.txt /tmp/requirements.txt
COPY . /code
WORKDIR /code
EXPOSE 8000

RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt
