import logging
import os


# SRC: https://stackoverflow.com/questions/384076/how-can-i-color-python-logging-output
class CustomFormatter(logging.Formatter):
    grey = "\x1b[38;21m"
    green = "\x1b[32;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s - %(levelname)s - %(message)s"  # type: ignore

    FORMATS = {
        logging.DEBUG: grey + format + reset,  # type: ignore
        logging.INFO: green + format + reset,  # type: ignore
        logging.WARNING: yellow + format + reset,  # type: ignore
        logging.ERROR: red + format + reset,  # type: ignore
        logging.CRITICAL: bold_red + format + reset,  # type: ignore
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, "%Y-%m-%d %H:%M:%S")
        return formatter.format(record)


def register_extension(app):
    if not os.path.exists("logs"):
        os.makedirs("logs")

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(CustomFormatter())
    logger.addHandler(console_handler)

    file_handler = logging.FileHandler("logs/logs.log")
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    )
    logger.addHandler(file_handler)

    app.logger = logger
    app.logger.info("Logger extension registered.")

    return app
