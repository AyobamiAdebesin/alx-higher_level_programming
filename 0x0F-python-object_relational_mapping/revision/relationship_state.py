#!/usr/bin/python3

import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, DateTime, MetaData, Table, Integer

my_metadata = MetaData()
Base = declarative_base(metadata=my_metadata)

class State(Base):
    """ A state class"""

    __tablename__ = "states"
    id = Column(Integer(), unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref='states', cascade="all, delete")
