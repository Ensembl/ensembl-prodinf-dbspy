FROM python:3.8.15-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --virtual .build-deps alpine-sdk python3-dev musl-dev libffi-dev \
    && apk add --no-cache mariadb-dev gcc

RUN addgroup -S appgroup && adduser -S appuser -G appgroup
RUN mkdir -p /usr/src/app
RUN chown -R appuser:appgroup /usr/src/app/


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_ROOT_USER_ACTION=ignore

USER appuser
WORKDIR /usr/src/app
COPY --chown=appuser:appgroup . /usr/src/app/
ENV PATH="/usr/src/app/venv/bin:$PATH"

RUN python -m venv /usr/src/app/venv/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

USER root
RUN apk --purge del .build-deps

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-c", "gunicorn_config.py", "--worker-tmp-dir", "/dev/shm", "ensembl.production.dbspy.main:app"]
