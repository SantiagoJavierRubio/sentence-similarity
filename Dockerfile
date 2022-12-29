# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["waitress-serve", "--call", "app:create_app"]
# CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", 
# "--worker-class", "gevent", "debug", "False", "--timeout", "600", "app:app"]