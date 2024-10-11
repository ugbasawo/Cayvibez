FROM python:alpine3.20

LABEL authors="SESUGH AGBADU"

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000


CMD [ "python","manage.py", "runserver", "0.0.0.0:8000" ]    