from typing import Union

from flask import current_app
from sqlalchemy.exc import SQLAlchemyError

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
                    
                    current_app.logger.info(f"User with [{key} : {value}] retrieved successfully")
                    return user

        for arg in args:

            if len(args) != 1:
                raise KeyError("Invalid number of arguments")
            if type(arg) == int:
                user = User.query.get(arg)
                if user is None:
                    raise KeyError(f"User with id {arg} does not exist")
                
                current_app.logger.info(f"User with id {arg} retrieved successfully")
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
                
                current_app.logger.info(f"Users with ids {arg} retrieved successfully")
                return users

            else:
                raise TypeError(f"Invalid argument type for {arg}")

        raise KeyError("No arguments provided")

    @staticmethod
    def update_nonsecure(**kwargs):
        """
        Update the user object with the provided non-secure attributes.

        Keyword Args:
            @user (required): The user object to update .
            @role (Optional): The new role for the user.
            @first_name (Optional): The new first name for the user.
            @last_name (Optional): The new last name for the user.

        Returns:
            User: The updated user object.

        Raises:
            KeyError: If the user object is not provided.
            KeyError: If an invalid number of arguments is provided.
            KeyError: If no valid attributes are provided to update.
            SQLAlchemyError: If there is an issue while updating, changes are reverted.
        """
        if "user" not in kwargs:
            raise KeyError("User object not provided")

        if len(kwargs) < 2:
            raise KeyError("Invalid number of arguments provided")

        user = kwargs["user"]
        null_items = 0
        update_struct = {
            "role": None,
            "first_name": None,
            "last_name": None,
        }

        for key, value in kwargs.items():
            if key in update_struct:
                update_struct[key] = value

        for key, value in update_struct.items():
            if value is None:
                null_items += 1
                if null_items == 3:
                    raise KeyError("No valid attributes provided to update")

            if value is not None:
                setattr(user, key, value)

        try:
            DB.session.commit()
        except SQLAlchemyError:
            DB.session.rollback()
            raise SQLAlchemyError(
                "There was an issue while updating the provided user! Changes have been reverted."
            )
        
        current_app.logger.info(f"User with id {user.id} updated successfully") 
        return user

    @staticmethod
    def update_secure():
        pass
