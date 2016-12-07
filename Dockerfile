FROM python:3.5.2-slim
MAINTAINER Paris Kasidiaris <paris@sourcelair.com>

ENV PORT 8000
ENV DATABASE_URL sqlite:////mnt/db.sqlite3
EXPOSE 8000
VOLUME ["/mnt/"]
WORKDIR "/usr/src/app"
RUN apt-get update &&\
    apt-get install -y make

COPY requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt

ADD . /usr/src/app

CMD ["honcho", "start"]

