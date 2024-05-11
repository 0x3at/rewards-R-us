import re


def is_password_valid(password):
    """
    Check if the password meets the complexity requirements.

    Password Complexity Rules:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    - Contains at least one special character from !@#$%^&*()-_=+{};:,<.>

    Args:
        password (str): The password to be validated.

    Returns:
        bool: True if the password is valid, False otherwise.
    """
    if len(password) < 8:
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"[a-z]", password):
        return False

    if not re.search(r"\d", password):
        return False
    if not re.search(r"[!@#$%^&*()\-_=+{};:,<.>]", password):
        return False

    return True
