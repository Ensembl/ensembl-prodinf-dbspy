FROM python:3.8.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --virtual .build-deps alpine-sdk python3-dev musl-dev libffi-dev \
    && apk add --no-cache mariadb-dev

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

RUN apk --purge del .build-deps

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-c", "gunicorn_config.py", "--worker-tmp-dir", "/dev/shm", "ensembl.production.dbspy.main:app"]
