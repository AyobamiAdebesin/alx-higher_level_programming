#!/usr/bin/python3
"""
A script that lists all State objects
that contain the letter 'a' from the
hbtn_0e_6_usa database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    # states = session.query(State).filter_by(State.name.like(%a%)).all()
    # NOTE: This a more optimized code other than the one below

    for state in session.query(State).order_by(State.id):
        if "a" in state.name:
            print("{}: {}".format(state.id, state.name))
