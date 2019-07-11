FROM python:3.7

WORKDIR /home/httpapp

COPY . .

RUN pip install -r requirements.txt

ENV PYTHONPATH /home/httpapp