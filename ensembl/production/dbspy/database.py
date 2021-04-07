from functools import lru_cache
from typing import List, Set, Tuple

import sqlalchemy as sa


SHOW_GLOBAL_STATUS = "SHOW GLOBAL STATUS"


SHOW_ALL_TABLE_STATUS = "SHOW TABLE STATUS FROM {dbname}"


SHOW_TABLE_STATUS = "SHOW TABLE STATUS FROM {dbname} LIKE '{pattern}'"


EXCLUDED_SCHEMAS = set(
    [
        "ensembl_accounts",
        "ensembl_dbcopy",
        "information_schema",
        "mysql",
        "PERCONA_SCHEMA",
        "performance_schema",
        "sys",
    ]
)


@lru_cache(maxsize=None)
def get_engine(
    hostname: str, port: int, user: str, password: str = ""
) -> sa.engine.Engine:
    uri = f"mysql://{user}:{password}@{hostname}:{port}"
    return sa.create_engine(uri, pool_recycle=3600)


def execute_sql(sql: str, hostname: str, port: int, user: str) -> List[Tuple[str, str]]:
    try:
        engine = get_engine(hostname, port, user)
        with engine.connect() as conn:
            result = conn.execute(sa.text(sql))
            return result.all()
    except sa.exc.OperationalError as err:
        raise RuntimeError(f"Cannot execute query: {err}") from err


def get_global_status(hostname: str, port: int, user: str) -> List[Tuple[str, str]]:
    return execute_sql(SHOW_GLOBAL_STATUS, hostname, port, user)


def get_allowed_databases(hostname: str, port: int, user: str) -> Set[str]:
    engine = get_engine(hostname, port, user)
    databases = sa.inspect(engine).get_schema_names()
    return set(databases).difference(EXCLUDED_SCHEMAS)


def get_table_status(
    hostname: str, port: int, user: str, database: str, table: str = None
) -> List[Tuple[str, str]]:
    allowed_databases = get_allowed_databases(hostname, port, user)
    if database not in allowed_databases:
        raise ValueError(f"Database name '{database}' not found")
    if table is None:
        result = execute_sql(
            SHOW_ALL_TABLE_STATUS.format_map({"dbname": database}), hostname, port, user
        )
    else:
        result = execute_sql(
            SHOW_TABLE_STATUS.format_map({"dbname": database, "pattern": table}),
            hostname,
            port,
            user,
        )
    return result
