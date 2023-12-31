FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY ./main.py /app

COPY ./mylib /app/mylib

EXPOSE 8000

ENTRYPOINT ["python3", "main.py"]

