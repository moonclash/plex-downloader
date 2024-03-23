FROM python:3.9.18-slim

WORKDIR /downloader

COPY ./src/requirements.txt .

RUN pip3 install -r requirements.txt

COPY ./src/ .

CMD [ "python3", "main.py" ]
