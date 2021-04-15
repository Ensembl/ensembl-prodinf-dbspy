[![Build Status](https://travis-ci.com/Ensembl/ensembl-prodinf-dbspy.svg?token=uixv5pZneCqzQNs8zEJr&branch=main)](https://travis-ci.com/Ensembl/ensembl-prodinf-dbspy)

EnsEMBL - Production DBSpy Web Application
==========================================

[FastAPI](https://fastapi.tiangolo.com/) Web application for monitoring MySQL database statistics.


System Requirements
-------------------

- Python 3.8+
- MySQL Client


Configuration
-------------

In order to connect to available MySQL servers, a text file in CSV format must
be provided to DBSpy (please refer to `hosts.csv` for an example of the format).
Such file must be readable by the web app and the path can be configured via the
environment variable `HOSTS_FILE` (Default: `HOSTS_FILE=./hosts.csv`)

Logging level can be set via `LOG_LEVEL` environment variable (e.g.
`LOG_LEVEL=debug`). Note that such variable will be read by default by Gunicorn.

Several Gunicorn config settings can be modified via the environment. Please
refer to `gunicorn_config.py` for documented usage.


Usage
-----

For development/testing purposes, the web server can be run using [Uvicorn](https://www.uvicorn.org/) directly, for example:
```
uvicorn ensembl.production.dbspy.main:app --reload
```
Please refer to [Uvicorn Documentation](https://www.uvicorn.org/deployment/) for
more information on running Uvicorn in development and production environments.

DBSpy can also run as a Docker container (see `Dockerfile`)


Testing
-------

Integration tests are implemented using Docker Compose and Pytest. Please refer
to `.travis.yml` for more insight on tests configuration.

In order to run tests manually, run the following commands:
```
pip install -r requirements-test.txt
pip install .
docker-compose -f tests/docker-compose.yml up -d
pytest tests
```

Please wait for Docker Compose to finish building the images on the first run
before running the tests with Pytest.
