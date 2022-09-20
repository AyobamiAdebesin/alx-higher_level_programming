#!/usr/bin/python3
"""
A script that contains the class definition of a
State and an instance of the declarative_base class
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Table, Integer, DateTime, Text, MetaData

my_metadata = MetaData()
Base = declarative_base(metadata=my_metadata)


class State(Base):
    """
    A class that represents a state with the id and name
    atribute
    """
    __tablename__ = 'states'
    id = Column(Integer(), unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
