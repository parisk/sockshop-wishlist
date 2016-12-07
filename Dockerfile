FROM 3.5.2-slim
MAINTAINER Paris Kasidiaris <paris@sourcelair.com>

ENV PORT 8000
ENV DATABASE_URL sqlite:////mnt/db.sqlite3
EXPOSE 8000
VOLUME ["/mnt/"]
CMD ["honcho", "start"]

