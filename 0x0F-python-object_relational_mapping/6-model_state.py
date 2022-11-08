#!/usr/bin/python3
import sqlalchemy
from sqlalchemy import (create_engine)
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://root:\
        olaseni1996@localhost/hbtn_0e_6_usa", pool_pre_ping=True)
    Base.metadata.create_all(engine)
