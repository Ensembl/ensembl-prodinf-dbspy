"""
Main module. Contains app loaded by Uvicorn worker.
"""

from typing import Optional

from fastapi import FastAPI, Request, HTTPException
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse

from ensembl.production.dbspy import config
from ensembl.production.dbspy.loggers import logger
from ensembl.production.dbspy.schemas import Info, ServerStatus, TablesStatus
from ensembl.production.dbspy.schemas import HTTPError, Message
from ensembl.production.dbspy.params import HostPath, PortPath, DBNamePath
from ensembl.production.dbspy.params import PatternQuery
from ensembl.production.dbspy.database import get_global_status, get_table_status
from ensembl.production.dbspy.database import DatabaseError
from ensembl.production.dbspy.utils import url_for


app = FastAPI(**config.OPENAPI)


logger.info(
    "Configuration: VERSION=%s, HOSTS_FILE=%s, LOG_LEVEL=%s",
    config.VERSION,
    config.HOSTS_FILE,
    config.LOG_LEVEL,
)


responses: Optional[dict] = {
    404: {"model": HTTPError, "description": "Resource not found"},
}


def get_host(hostname: str, port: int) -> dict:
    """Utility function to retrieve host details from config.
    Raise HTTP 404 Error code, if host/port not found.
    """
    host = config.HOSTS.get((hostname, port))
    if not host:
        raise HTTPException(
            status_code=404,
            detail=[Message(msg="Server name or port not found").dict()],
        )
    return host


@app.get("/", response_model=Info, tags=["server_info"])
def info():
    """Info View. Returns server's version. Can be used as simple healthcheck"""
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
    """Server Status View. Returns MySQL Global Server Status variables for a given MySQL Server"""
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
    """Table Status View. Returns MySQL Table Status variables for a given MySQL Database"""
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


@app.exception_handler(DatabaseError)
async def database_exception_handler(request: Request, exc: DatabaseError):
    msg = f"Error: Cannot execute query to database."
    log = f"{request.method}: {request.url}"
    logger.critical("%s: %s", log, exc)
    return JSONResponse(status_code=502,
                        content={"detail": [Message(msg=msg).dict()]})

