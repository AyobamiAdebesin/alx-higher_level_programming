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
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@\
            localhost:3306/{sys.argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # states = session.query(State).filter_by(State.name.like(%a%)).all()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        if 'a' in state:
            print(f"{state.id}: {state.name}")
