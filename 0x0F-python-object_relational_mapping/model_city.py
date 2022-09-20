#!/usr/bin/python3
"""
A script that defines a class for the City
table in the database
"""
from sqlalchemy.ext import declarative_base
from sqlalchemy import String, Text, Float, DateTime
from sqlalchemy import MetaData, Column, Integer, ForeignKey
from model_state import Base, State
my_metadata = MetaData()
Base = declarative_base(metadata= my_metadata)

class City(Base):
    __tablename__ = "cities"
    id = Column(Integer(), unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey(State.c.id), nullable=False)
