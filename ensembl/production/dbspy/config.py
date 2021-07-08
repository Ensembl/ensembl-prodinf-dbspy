"""
Configuration module. Meant to be read-only.
"""

import csv
import os


with open("VERSION", "r") as f:
    VERSION = f.read()


LOG_LEVEL = os.getenv("LOG_LEVEL", "info").lower()


OPENAPI = {
    "title": "DBSpy",
    "version": "1.0",
    "description": "DBSpy Schema",
    "openapi_tags": [
        {"name": "server_info", "description": "Server information"},
        {"name": "database_status", "description": "Database status"},
    ],
}


HOSTS_FILE = os.getenv("HOSTS_FILE", "hosts.csv")


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
