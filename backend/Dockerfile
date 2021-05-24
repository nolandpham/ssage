FROM python:3.7-alpine

COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade -r /tmp/requirements.txt
RUN rm -rf /var/cache/apk/*
RUN mkdir /apps
WORKDIR /apps

CMD ["python", "/apps/main.py"]

EXPOSE 5000

ADD . /apps
