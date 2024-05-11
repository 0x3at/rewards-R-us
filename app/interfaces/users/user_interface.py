# type: ignore
from werkzeug.security import check_password_hash


from ...models import Users
from ...utils.decorators import can_throw
from ...extensions.database import DB as db


class UserInterface:

    @staticmethod
    @can_throw
    def add(
        username,
        password_hash,
        balance,
        role,
        email,
        mobile,
        first_name,
        last_name,
        company_id,
    ):
        user = Users(
            username=username,
            password_hash=password_hash,
            balance=balance,
            role=role,
            email=email,
            mobile=mobile,
            first_name=first_name,
            last_name=last_name,
            company_id=company_id,
        )
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

        return user

    @staticmethod
    @can_throw
    def delete(id):
        try:
            user = Users.query.get(id)
            db.session.delete(user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    @can_throw
    def update(user, updated_fields):
        update_struct = {
            "username": None,
            "password_hash": None,
            "balance": None,
            "role": None,
            "email": None,
            "mobile": None,
            "first_name": None,
            "last_name": None,
            "company_id": None,
        }
        for key, value in updated_fields.items():
            if update_struct[key]:
                update_struct[key] = value
            if value is not None:
                setattr(user, key, value)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

        return user

    @staticmethod
    @can_throw
    def get_all():
        all_users = [user.sanitize() for user in Users.query.all()]
        return all_users

    @staticmethod
    @can_throw
    def get_one(id):
        user = Users.query.get(id)
        if user is None:
            raise Exception

        user.sanitize()
        return user

    @staticmethod
    @can_throw
    def check_username_availability(username):
        try:
            user = Users.query.filter_by(username=username).first()
        except Exception as e:
            raise e

        is_available = True if user is None else False
        return is_available

    @staticmethod
    @can_throw
    def check_password(username, password):
        try:
            user = Users.query.filter_by(username=username).first()
        except Exception as e:
            raise e

        return (
            False if user is None else check_password_hash(user.password_hash, password)
        )

    @staticmethod
    @can_throw
    def get_user_by_username(username):
        try:
            user = Users.query.filter_by(username=username).first()
        except Exception as e:
            raise e

        return user
