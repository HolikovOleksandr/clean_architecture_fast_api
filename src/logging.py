import logging
from enum import Enum

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"


class LogLevel(Enum): 
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL


def setup_logger(log_level: LogLevel) -> logging.Logger:
    if log_level not in LogLevel:
        logging.basicConfig(level=logging.error, format=LOG_FORMAT)
        return
    
    if log_level == LogLevel.DEBUG:
        logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)
        return
    
    logging.basicConfig(level=log_level.value, format=LOG_FORMAT)