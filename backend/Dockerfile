FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y \
    netcat

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000