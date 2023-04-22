#!/usr/bin/python3
"""
This python module returns the state id of a given state name from
hbtn_0e_6_usa using sqlalchemy ORM in interacting with the database
"""

from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine


if __name__ == '__main__':
    if (len(argv) != 5):
        exit()
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    stateSearchName = (argv[4],)

    # create a connection Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # quering the database in search of a given state name
    states = session.query(State).filter_by(name=stateSearchName).first()

    # printing the result
    if states:
        print(states.id)
    else:
        print("Not found")
