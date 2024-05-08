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
        # Create some business units
        business_unit_1 = BusinessUnit(created_at=int(time.time()))
        business_unit_2 = BusinessUnit(created_at=int(time.time()))

        # Add the business units to the database
        DB.session.add(business_unit_1)
        DB.session.add(business_unit_2)
        DB.session.commit()

        # Create some users and assign them to business units
        user_1 = User(username='user1', password_hash='password1', balance=100.0, role='role1',
                      created_at=int(time.time()), email='user1adscsd@example.com', mobile='1234ae56789',
                      first_name='User', last_name='One', business_unit_id=business_unit_1.id)
        user_2 = User(username='user2', password_hash='password2', balance=200.0, role='role2',
                      created_at=int(time.time()), email='user2@asdexample.com', mobile='9czx87654321',
                      first_name='Usr', last_name='Two', business_unit_id=business_unit_2.id)
        user_3 = User(username='usedasdar1', password_hash='password1', balance=100.0, role='role1',
                      created_at=int(time.time()), email='user1312ads313@example.cm', mobile='2343123156789',
                      first_name='Usdasdadfer', last_name='One', business_unit_id=business_unit_3.id)
        user_4 = User(username='user2', password_hash='password2', balance=200.0, role='role2',
                      created_at=int(time.time()), email='user1231312@example.com', mobile='987312312654321',
                      first_name='Usasddaer', last_name='Two', business_unit_id=business_unit_4.id)
        user_5 = User(username='user1rrrrsar', password_hash='password1', balance=100.0, role='role1',
                      created_at=int(time.time()), email='user1@123312example.com', mobile='12345678912312',
                      first_name='Userrdfvszr', last_name='One', business_unit_id=business_unit_5.id)
        user_6 = User(username='user2rr', password_hash='password2', balance=200.0, role='role2',
                      created_at=int(time.time()), email='user2@exa12312mple.com', mobile='987612312354321',
                      first_name='Userrr', last_name='Two', business_unit_id=business_unit_6.id)
        user_7 = User(username='user1r', password_hash='password1', balance=100.0, role='role1',
                      created_at=int(time.time()), email='user1@exasdadample.com', mobile='12312456789',
                      first_name='Userrrr', last_name='One', business_unit_id=business_unit_7.id)
        user_8 = User(username='user2r', password_hash='password2', balance=200.0, role='role2',
                      created_at=int(time.time()), email='userasda2@example.com', mobile='987654321',
                      first_name='Usfsafderr', last_name='Two', business_unit_id=business_unit_8.id)

        # Add the users to the database
        DB.session.add(user_1)
        DB.session.add(user_3)
        DB.session.add(user_4)
        DB.session.add(user_5)
        DB.session.add(user_6)
        DB.session.add(user_7)
        DB.session.add(user_8)
        DB.session.commit()

app.run(debug=True, port=8080)
