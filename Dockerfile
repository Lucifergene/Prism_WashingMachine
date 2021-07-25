FROM python:3.6

ADD requirements.txt /

RUN pip install -r /requirements.txt &&\
    apt-get update -y

ADD . /app

WORKDIR /app

EXPOSE 5000
CMD [ "python" , "app.py"]