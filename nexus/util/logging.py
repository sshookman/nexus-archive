import logging
from datetime import date

LOG_LEVELS = list(logging._nameToLevel.keys())
FORMAT = "[%(asctime)s] [%(levelname)s] <%(name)s> %(message)s"
DATE_FORMAT = "%Y-%m-%d %I:%M:%S"

class NexusLogger:
    """
    NexusLogger Class
    This class provides a simple logging mechanism that allows for logging to std out by default,
    and also allows for logging to a file as well.
    """

    logger = None

    def __init__(self, name, level=None, file_out=None, file_date=True):
        """
        Initialize the logger based on the log level as well as how and if it logs to a file
        Parameters
        ----------
        name : string
            The name of the specific class from which the logging is being performed (often passed
            as `__name__`)
        level : string
            The log level at which logging will be captured (["DEBUG", "INFO", "WARNING", "ERROR",
            "CRITICAL"])
        file_out : string
            The name of the file where logs will be appended (if not provided, no log file is used)
        file_date : boolean
            If true: the current data will be appended to the log file in order to separate log
            output
        """

        handlers = [logging.StreamHandler()]

        if (file_out is not None):
            filename = f"{file_out}_{date.today()}.log" if file_date else f"{file_out}.log"
            handlers += [logging.FileHandler(filename, delay=True)]

        if (level is not None):
            logging.basicConfig(format=FORMAT, level=level, datefmt=DATE_FORMAT, handlers=handlers)

        self.logger = logging.getLogger(name)

    def debug(self, message):
        """
        Log debug level messages
        Parameters
        ----------
        message : string
            The message to be logged
        """

        self.logger.debug(message)

    def info(self, message):
        """
        Log info level messages
        Parameters
        ----------
        message : string
            The message to be logged
        """
        self.logger.info(message)

    def warning(self, message):
        """
        Log warning level messages
        Parameters
        ----------
        message : string
            The message to be logged
        """
        self.logger.warning(message)

    def error(self, message):
        """
        Log error level messages
        Parameters
        ----------
        message : string
            The message to be logged
        """
        self.logger.error(message)

    def critical(self, message):
        """
        Log critical level messages
        Parameters
        ----------
        message : string
            The message to be logged
        """
        self.logger.critical(message)
