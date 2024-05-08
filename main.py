#type: ignore
from app import create_app
import time
from flask import current_app
from app.extensions.database import DB
from app.models import User, BusinessUnit


app = create_app()

@app.route("/")
def add_data_to_tables():
    with current_app.app_context():
        # # Create some business units
        # business_unit_1 = BusinessUnit(created_at=int(time.time()))
        # business_unit_2 = BusinessUnit(created_at=int(time.time()))

        # # Add the business units to the database
        # DB.session.add(business_unit_1)
        # DB.session.add(business_unit_2)
        # DB.session.commit()

        # # Create some users and assign them to business units
        # user_1 = User(username='user1', password_hash='password1', balance=100.0, role='role1',
        #               created_at=int(time.time()), email='user1adscsd@example.com', mobile='1234ae56789',
        #               first_name='User', last_name='One', business_unit_id=business_unit_1.id)
        # user_2 = User(username='user2', password_hash='password2', balance=200.0, role='role2',
        #               created_at=int(time.time()), email='user2@asdexample.com', mobile='9czx87654321',
        #               first_name='Usr', last_name='Two', business_unit_id=business_unit_2.id)

        # # Add the users to the database
        # DB.session.add(user_1)
        # DB.session.add(user_2)
        # DB.session.commit()

app.run(debug=True, port=8080)
