# type: ignore
from ...models import Companies

from ...extensions.database import DB as db

from ...utils.decorators import can_throw


class CompanyInterface:

    @staticmethod
    @can_throw
    def add(name):
        try:
            company = Companies(name=name)
            db.session.add(company)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

        return company

    @staticmethod
    @can_throw
    def update(company, updated_fields):
        update_struct = {"name": None}
        for key, value in updated_fields.items():
            if update_struct[key]:
                update_struct[key] = value
            if value is not None:
                setattr(company, key, value)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
        return company

    @staticmethod
    @can_throw
    def delete(company):
        try:
            db.session.delete(company)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
        return company

    @staticmethod
    @can_throw
    def get_one(id):
        try:
            company = Companies.query.get(id)
        except Exception as e:
            raise e

        return company

    @staticmethod
    @can_throw
    def get_all():
        try:
            all_companies = [
                company.sanitize()
                for company in Companies.query.all()
                if company is not None
            ]
        except Exception as e:
            raise e

        return all_companies
