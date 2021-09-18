FROM python:3.9

RUN apt update \
    && apt install -y mc

RUN mkdir -p /usr/src

WORKDIR usr/src

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0:8080"]

