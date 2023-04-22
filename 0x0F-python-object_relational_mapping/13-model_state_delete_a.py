#!/usr/bin/python3
"""
This python script deletes a record given a condition
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
    delete_state = session.query(State).filter(State.name.like('%a%')).all()

    for state in delete_state:
        session.delete(state)
    session.commit()
    session.close()
