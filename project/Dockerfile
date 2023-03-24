FROM python:3.10-slim

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /app
RUN mkdir -pv /var/log/gunicorn/
RUN mkdir -pv /var/run/gunicorn/
COPY . .
