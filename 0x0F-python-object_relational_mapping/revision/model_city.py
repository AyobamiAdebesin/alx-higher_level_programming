#!/usr/bin/python3

import sqlalchemy
from sqlalchemy import Column, Table, Integer, DateTime, MetaData, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

my_metadata = MetaData()
Base = declarative_base(metadata=my_metadata)

class City(Base):
    __tablename__ = "cities"

    id = Column(Integer(), nullable=False, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    