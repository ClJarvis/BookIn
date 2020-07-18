import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *

engine = create_engine('sqlite:///tutorial.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

user = User(username="123452020",password="1/1/2020")
session.add(user)

user = User(username="testt357",password="Thisthingon?")
session.add(user)

user = User(username="tk421",password="ou812")
session.add(user)

# commit the record the database
session.commit()

session.commit()