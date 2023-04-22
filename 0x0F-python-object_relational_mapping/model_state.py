#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sys import argv

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = Column("id", Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column("name", String(128), nullable=False)


engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
    argv[1], argv[2], argv[3]))
Base.metadata.create_all(engine)
