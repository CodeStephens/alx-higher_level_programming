#!/usr/bin/python3
"""
This python module adds a new record to the database and returns the state id
"""

from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    # create a connection Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Creating a new state object
    new_state = State(name="Louisiana")

    session.add(new_state)
    session.commit()

    # printing the result
    print(new_state.id)
