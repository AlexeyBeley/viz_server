FROM python:3.6.5-slim

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY . /app
WORKDIR /app

ENTRYPOINT ["./gunicorn_starter.sh"]

#docker run -d -p 8000:8000 backend

