from typing import Union

from ..models import User

from ..extensions.database import DB


class UserInterface:
    """Interface for querying and retrieving data from the User table."""

    DB_session = DB.session

    @staticmethod
    def get(*args: int | list[int], **kwargs: str):
        """
        Get a user OR list of users from the User table.
        Requires at least one arg or keyword arg.

        Args:
            @param1 (Optional[int]): The id of the user to retrieve.
            @param2 (Optional[list[int]]): A list of user ids to retrieve.

        Keyword Args:
            @username (Optional[str]): The username of the user to retrieve.
            @email (Optional[str]): The email of the user to retrieve.
            @mobile (Optional[str]): The mobile number of the user to retrieve.

        Returns:
            User: The user with the provided identifier.
            list[User]: A list of users with the provided ids.

        Raises:
            KeyError: If no arguments or too many args are provided.
            KeyError: If the user(s) with the provided id does not exist.
            KeyError: If the user with the provided username/email/mobile does not exist.
            TypeError: If the argument type is invalid compared to the Tables Column Datatype.
        """

        if kwargs:
            if len(args) != 0:
                raise KeyError("Invalid number of arguments")

            for key, value in kwargs.items():
                if type(value) != str:
                    raise TypeError(f"Invalid argument type for {key}")

                if key == "username" or key == "email" or key == "mobile":
                    user = User.query.filter_by(**{key: value}).first()
                    if user is None:
                        raise KeyError(f"User with [{key} : {value}] does not exist")
                    return user

        for arg in args:
            if len(args) != 1:
                raise KeyError("Invalid number of arguments")
            if type(arg) == int:
                user = User.query.get(arg)
                if user is None:
                    raise KeyError(f"User with id {arg} does not exist")
                return user

            elif type(arg) == list:
                users: list[User] = []
                for user_id in arg:
                    if type(user_id) == int:
                        user = User.query.get(user_id)
                        if user is not None:
                            users.append(user)

                if len(users) == 0:
                    raise KeyError(f"None of the users with ids {arg} exist")
                return users

            else:
                raise TypeError(f"Invalid argument type for {arg}")

        raise KeyError("No arguments provided")
