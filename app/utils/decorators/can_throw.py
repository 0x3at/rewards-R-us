import inspect

from ...types.exceptions import LoggedError


def can_throw(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        argspec = inspect.getfullargspec(func)
        args_passed = argspec.args
        kwargs_passed = kwargs

        try:
            return func(*args, **kwargs)

        except Exception as e:
            raise LoggedError(
                func_name=func_name,
                message=str(
                    f"Error handler has caught an error during execution of{func_name}"
                ),
                exception=e,
                args_passed=args_passed,
                kwargs_passed=kwargs_passed,
            )

    return wrapper
