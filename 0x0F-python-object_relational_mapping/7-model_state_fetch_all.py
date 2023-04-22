#!/usr/bin/python3
"""
This python module lists all State objects from the database hbtn_0e_6_usa
using sqlalchemy ORM in interacting with the database
"""

from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")
