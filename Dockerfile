FROM python:3.5.2-slim
MAINTAINER Paris Kasidiaris <paris@sourcelair.com>

ENV PORT 8000
ENV DATABASE_URL sqlite:////mnt/db.sqlite3
EXPOSE 8000
VOLUME ["/mnt/"]
WORKDIR "/usr/src/app"

ADD . /usr/src/app

RUN pip install -r requirements.txt

CMD ["honcho", "start"]

