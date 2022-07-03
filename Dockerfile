FROM python:3.8-slim

COPY . /app
WORKDIR /app

RUN pip install .

CMD [ "python", "shortener/main.py" ]