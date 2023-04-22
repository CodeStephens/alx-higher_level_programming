#!/usr/bin/python3
"""
This python script deletes a record given a condition
"""

from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from model_city import City


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    # create a connection Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Creating a new state object
    all_cities = session.query(City, State).join(State).order_by(City.id)

    for city, state in all_cities:
        print(f'{state.name}: ({city.id}) {city.name}')

    session.close()
