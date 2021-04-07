from typing import Optional

from fastapi import FastAPI, Request, HTTPException
from fastapi.openapi.utils import get_openapi

from ensembl.production.dbspy import config
from ensembl.production.dbspy.logging import logger
from ensembl.production.dbspy.schemas import Info, ServerStatus, TablesStatus
from ensembl.production.dbspy.schemas import HTTPError, Message
from ensembl.production.dbspy.params import HostPath, PortPath, DBNamePath
from ensembl.production.dbspy.params import PatternQuery
from ensembl.production.dbspy.database import get_global_status, get_table_status
from ensembl.production.dbspy.utils import url_for


app = FastAPI(**config.OPENAPI)


responses: Optional[dict] = {
    404: {"model": HTTPError, "description": "Resource not found"},
}


def get_host(hostname: str, port: int) -> dict:
    host = config.HOSTS.get((hostname, port))
    if not host:
        raise HTTPException(
            status_code=404,
            detail=[Message(msg="Server name or port not found").dict()],
        )
    return host


@app.get("/", response_model=Info, tags=["server_info"])
def info():
    return Info(name=config.OPENAPI["title"], server_version=config.VERSION)


@app.get(
    "/status/global/{hostname}/{port}",
    response_model=ServerStatus,
    response_model_exclude_unset=True,
    responses=responses,
    tags=["database_status"],
)
def server_status(
    request: Request,
    hostname: str = HostPath(title="MySQL Server host name"),
    port: int = PortPath(title="MySQL Server port number"),
):
    host = get_host(hostname, port)
    user = host["user"]
    result = get_global_status(hostname, port, user)
    dict_result = dict(result)
    path_params = dict(hostname=hostname, port=port)
    self_url = url_for(request, "server_status", path_params)
    server = f"{hostname}:{port}"
    return ServerStatus(_self=self_url, mysql_server=server, result=dict_result)


@app.get(
    "/status/table/{hostname}/{port}/{database}",
    response_model=TablesStatus,
    responses=responses,
    tags=["database_status"],
)
def table_status(
    request: Request,
    hostname: str = HostPath(title="MySQL Server host name"),
    port: int = PortPath(title="MySQL Server port number"),
    database: str = DBNamePath(title="Database name"),
    table: Optional[str] = PatternQuery(title="Table name (MySQL pattern)"),
):
    host = get_host(hostname, port)
    user = host["user"]
    try:
        results = get_table_status(hostname, port, user, database, table)
    except ValueError as err:
        raise HTTPException(status_code=404, detail=[Message(msg=str(err)).dict()])
    path_params = dict(hostname=hostname, port=port, database=database)
    query_params = dict(table=table)
    self_url = url_for(request, "table_status", path_params, query_params)
    return TablesStatus(_self=self_url, results=results)
