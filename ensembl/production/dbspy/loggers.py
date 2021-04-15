"""
Custom loggers module.
"""

import logging

from ensembl.production.dbspy import config


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
