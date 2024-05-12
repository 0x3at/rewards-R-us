# type: ignore
import time

from ...models import Invites
from ...utils.decorators import can_throw
from ...extensions.database import DB as db


class InviteInterface:
    @staticmethod
    @can_throw
    def add(company_id, expiration, role, email):
        try:
            invite = Invites(
                company_id=company_id, expiration=expiration, role=role, email=email
            )
            db.session.add(invite)
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            raise e

        return invite

    @staticmethod
    @can_throw
    def get_invite_by_code(code):
        try:
            invite = Invites.query.filter_by(code=code).first()
        except Exception as e:
            raise e

        return invite

    @staticmethod
    @can_throw
    def consume_invite(invite):
        try:
            invite.consumed = True
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

        return invite
    
    @staticmethod
    @can_throw
    def is_invite_valid(code):
        try:
            invite = Invites.query.filter_by(code=code).first()
            
            if invite is None:
                return False
            
            if invite.consumed:
                return False
            
            if invite.expiration < time.time():
                return False
            
        except Exception as e:
            raise e

        return True

    @staticmethod
    @can_throw
    def delete_invite(invite):
        try:
            db.session.delete(invite)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

        return invite
