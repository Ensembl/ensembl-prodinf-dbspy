"""
Custom loggers module.
"""

import logging

from ensembl.production.dbspy import config


#  date_fmt = "%Y-%m-%d %H:%M:%S %z"
#  default_fmt = "[%(asctime)s] %(name)-14s %(levelprefix)-9s %(message)s"
#  access_fmt = '[%(asctime)s] %(name)-14s %(levelprefix)-9s %(client_addr)s - "%(request_line)s" %(status_code)s'

#  LOGGING_CONFIG = {
#      "version": 1,
#      "disable_existing_loggers": False,
#      "formatters": {
#          "default": {
#              "()": "uvicorn.logging.DefaultFormatter",
#              "fmt": default_fmt,
#              "datefmt": date_fmt,
#          },
#          "access": {
#              "()": "uvicorn.logging.AccessFormatter",
#              "fmt": access_fmt,
#              "datefmt": date_fmt,
#          },
#      },
#      "handlers": {
#          "default": {
#              "class": "logging.StreamHandler",
#              "formatter": "default",
#              "stream": "ext://sys.stderr",
#          },
#          "access": {
#              "class": "logging.StreamHandler",
#              "formatter": "access",
#              "stream": "ext://sys.stdout",
#          },
#      },
#      "loggers": {
#          "uvicorn": {"level": config.LOG_LEVEL, "handlers": ["default"]},
#          "uvicorn.error": {"level": config.LOG_LEVEL},
#          "uvicorn.access": {
#              "level": config.LOG_LEVEL,
#              "propagate": False,
#              "handlers": ["access"],
#          },
#      },
#  }

#  logging.config.dictConfig(LOGGING_CONFIG)
log_levels = {
    'critical': logging.CRITICAL,
    'error': logging.ERROR,
    'warning': logging.WARNING,
    'info': logging.INFO,
    'debug': logging.DEBUG,
}
log_level = log_levels.get(config.LOG_LEVEL, logging.INFO)
logging.getLogger("uvicorn").setLevel(log_level)
logger = logging.getLogger("uvicorn.error")
logger.setLevel(log_level)
