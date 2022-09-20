#!/usr/bin/python3
"""
A script that updates name of a State object
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    stateUpdated = session.query(State).filter(State.id == 2).first()
    if stateUpdated:
        stateUpdated.name = "New Mexico"
        session.commit()
