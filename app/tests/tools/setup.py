import json
from ...models import Companies, Users, Transactions, Products


def setup_qa_db(session):
    with open("app/tests/tools/mocks/companies.json", "r") as file:
        companies_data = json.load(file)
        for company_data in companies_data:
            company = Companies(**company_data)
            session.add(company)

    with open("app/tests/tools/mocks/users.json", "r") as file:
        users_data = json.load(file)
        for user_data in users_data:
            user = Users(**user_data)
            session.add(user)

    with open("app/tests/tools/mocks/products.json", "r") as file:
        products_data = json.load(file)
        for product_data in products_data:
            product = Products(**product_data)
            session.add(product)

    with open("app/tests/tools/mocks/transactions.json", "r") as file:
        transactions_data = json.load(file)
        for transaction_data in transactions_data:
            transaction = Transactions(**transaction_data)
            session.add(transaction)

    session.commit()
