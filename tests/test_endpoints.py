# See the NOTICE file distributed with this work for additional information
#   regarding copyright ownership.
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#       http://www.apache.org/licenses/LICENSE-2.0
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
import time

import pytest
from fastapi.testclient import TestClient
import sqlalchemy as sa

from ensembl.production.dbspy.main import app


DB_NAME = "test"
MYSQL_HOST = "127.0.0.1"
MYSQL_PORT = "3306"
MYSQL_USER = "root"
MYSQL_CONNECT_RETRIES = 60
MYSQL_RETRY_DELAY = 1


client = TestClient(app)


@pytest.fixture
def db_conn():
    retries = MYSQL_CONNECT_RETRIES
    mysql_uri = f"mysql://{MYSQL_USER}@{MYSQL_HOST}:{MYSQL_PORT}"
    engine = sa.create_engine(mysql_uri)
    while True:
        try:
            conn = engine.connect()
        except sa.exc.OperationalError as err:
            if retries == 0:
                engine.dispose()
                raise TimeoutError(f"Cannot connect to {mysql_uri}") from err
            time.sleep(MYSQL_RETRY_DELAY)
            retries -= 1
        else:
            break
    conn.execute(sa.text(f"DROP DATABASE IF EXISTS {DB_NAME}; CREATE DATABASE {DB_NAME};"))
    try:
        yield conn
    finally:
        conn.close()
        engine.dispose()


def create_tables(conn, table_names):
    for table_name in table_names:
        conn.execute(sa.text(f"USE {DB_NAME}; CREATE TABLE {table_name} (col_1 INT);"))


def test_info_view_ok():
    response = client.get("/")
    assert response.status_code == 200


def test_server_status_ok(db_conn):
    response = client.get(f"/status/global/{MYSQL_HOST}/{MYSQL_PORT}")
    assert response.status_code == 200
    response_body = response.json()
    assert response_body["mysql_server"] == f"{MYSQL_HOST}:{MYSQL_PORT}"
    assert len(response_body["result"]) == 307


def test_server_status_not_found(db_conn):
    response = client.get(f"/status/global/unknown-host/{MYSQL_PORT}")
    assert response.status_code == 404
    unknown_port = 3333
    response = client.get(f"/status/global/{MYSQL_HOST}/{unknown_port}")
    assert response.status_code == 404


def test_server_status_unprocessable(db_conn):
    response = client.get(f"/status/global/invalid+host/{MYSQL_PORT}")
    assert response.status_code == 422
    invalid_port = 123456
    response = client.get(f"/status/global/{MYSQL_HOST}/{invalid_port}")
    assert response.status_code == 422
    response = client.get(f"/status/global/{MYSQL_HOST}/not-a-port")
    assert response.status_code == 422


def test_table_status_ok(db_conn):
    table_names = ["table_1", "table_2"]
    create_tables(db_conn, table_names)
    response = client.get(f"/status/table/{MYSQL_HOST}/{MYSQL_PORT}/{DB_NAME}")
    assert response.status_code == 200
    response_body = response.json()
    assert len(response_body["results"]) == 2
    result_names = sorted(map(lambda x: x["Name"], response_body["results"]))
    assert result_names == table_names


def test_table_status_query_ok(db_conn):
    table_names = ["table_1", "table_2"]
    create_tables(db_conn, table_names)
    response = client.get(f"/status/table/{MYSQL_HOST}/{MYSQL_PORT}/{DB_NAME}?table=table_1")
    assert response.status_code == 200
    response_body = response.json()
    assert len(response_body["results"]) == 1
    result_names = list(map(lambda x: x["Name"], response_body["results"]))
    assert result_names == ["table_1"]


def test_table_status_not_found(db_conn):
    response = client.get(f"/status/table/{MYSQL_HOST}/{MYSQL_PORT}/unknown_db")
    assert response.status_code == 404
    response = client.get(f"/status/table/{MYSQL_HOST}/{MYSQL_PORT}/information_schema")
    assert response.status_code == 404


def test_table_status_unprocessable(db_conn):
    response = client.get(f"/status/table/{MYSQL_HOST}/{MYSQL_PORT}/invalid-db")
    assert response.status_code == 422
    response = client.get(f"/status/table/{MYSQL_HOST}/{MYSQL_PORT}/{DB_NAME}?table=invalid-table")
    assert response.status_code == 422


def test_database_connection_error():
    response = client.get(f"/status/global/localhost/{MYSQL_PORT}")
    assert response.status_code == 502
