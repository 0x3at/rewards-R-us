# type: ignore
from ...models import Invites
from ...utils.decorators import can_throw
from ...extensions.database import DB as db


class InviteInterface:
    @staticmethod
    @can_throw
    def add(company_id, expiration, role, email):
        invite = Invites(
            company_id=company_id, expiration=expiration, role=role, email=email
        )
        db.session.add(invite)
        db.session.commit()
        return invite

    @staticmethod
    @can_throw
    def get_invite_by_code(code):
        return Invites.query.filter_by(code=code).first()

    @staticmethod
    @can_throw
    def delete_invite(invite):
        db.session.delete(invite)
        db.session.commit()
        return invite
