import csv
import os

from ensembl.production.dbspy.logging import logger


VERSION = "1.0.0"


OPENAPI = {
    "title": "DBSpy",
    "version": "1.0.0",
    "description": "DBSpy Schema",
    "openapi_tags": [
        {"name": "server_info", "description": "Server information"},
        {"name": "database_status", "description": "Database status"},
    ],
}


HOSTS_FILE = os.environ.get("HOSTS_FILE", "hosts.csv")


def load_hosts(reader: csv.DictReader) -> dict:
    return {
        (host["name"], int(host["port"])): {
            "user": host["mysql_user"],
            "server": host["virtual_machine"],
            "owner": host["mysqld_file_owner"],
            "active": bool(int(host["active"])),
        }
        for host in reader
    }


def get_hosts() -> dict:
    with open(HOSTS_FILE, newline="") as hosts_csv:
        reader = csv.DictReader(hosts_csv)
        hosts = load_hosts(reader)
    return hosts


HOSTS = get_hosts()


logger.info("Configuration: VERSION=%s, HOSTS_FILE=%s", VERSION, HOSTS_FILE)
