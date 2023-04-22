#!/usr/bin/python3
"""
This python module lists all State objects that contains 'a'from the database
hbtn_0e_6_usa using sqlalchemy ORM in interacting with the database
"""

from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine


if __name__ == '__main__':
    if (len(argv) != 4):
        exit()
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    # create a connection Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # quering the database for all states with letter 'a'
    states = session.query(State).filter(State.name.like('%a%')).\
        order_by(State.id)

    # printing the result
    for state in states:
        print(f'{state.id}: {state.name}')
