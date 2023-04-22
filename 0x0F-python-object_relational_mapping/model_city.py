#!/usr/bin/python3
"""
This python module defines a new class(table) 'cities' connected to a new
database hbtn_0e_14_usa
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """"
    Declaration of class to mimick a table in the SQL database
    """
    __tablename__ = 'cities'
    id = Column("id", Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id", Integer, ForeignKey(
        'states.id'), nullable=False)
