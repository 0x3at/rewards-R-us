import secrets
import time
import traceback

from flask import current_app


class LoggedError(Exception):
    def __init__(
        self,
        func_name: str,
        message: str,
        exception: Exception,
        args_passed: list[str],
        kwargs_passed: dict,
    ):
        self.id = secrets.token_hex(8)
        self.func_name = func_name
        self.message = message
        self.timestamp = time.time()
        self.exception = exception
        self.kwargs_passed = kwargs_passed
        self.args_passed = args_passed
        self.log_error()

    def log_error(self):
        log_message = f"Error ID: {self.id}\n"
        log_message += f"Function Name: {self.func_name}\n"
        log_message += f"Message: {self.message}\n"
        log_message += f"Timestamp: {self.timestamp}\n"
        log_message += f"Exception Type: {type(self.exception).__name__}\n"
        log_message += f"Exception Message: {str(self.exception)}\n"
        log_message += f"Arguments Passed: {self.args_passed}\n"
        log_message += f"Keyword Arguments Passed: {self.kwargs_passed}\n"
        log_message += f"Stack Trace:\n"
        log_message += "".join(traceback.format_tb(self.exception.__traceback__))

        current_app.logger.error(log_message)
