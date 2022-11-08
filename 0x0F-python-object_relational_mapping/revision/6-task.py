#!/usr/bin/python3

from sqlalchemy import create_engine
import sys
from model_state import State, Base

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://root:olaseni1996@localhost/hbtn_0e_6_usa", pool_pre_ping=True)
    Base.metadata.create_all(engine)
