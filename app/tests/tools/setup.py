import json

def setup_qa_db(session,UserModel,CompanyModel):
    with open('app/tests/tools/data/companies.json', 'r') as file:
        companies_data = json.load(file)
        for company_data in companies_data:
            company = CompanyModel(**company_data)
            session.add(company)

    with open('app/tests/tools/data/users.json', 'r') as file:
        users_data = json.load(file)
        for user_data in users_data:
            user = UserModel(**user_data)
            session.add(user)

    session.commit()