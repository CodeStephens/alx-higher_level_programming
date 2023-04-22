#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = Column("id", Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column("name", String(128), nullable=False)


engine = create_engine('mysql://root:Mestika1*@localhost:3306/hbtn_0e_6_usa')
Base.metadata.create_all(engine)
