#!/usr/bin/python3

import sqlalchemy
from relationship_state import Base, State
from sqlalchemy import Column, String, DateTime, MetaData, Integer, Float, ForeignKey


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer,  ForeignKey("states.id"), nullable=False)
