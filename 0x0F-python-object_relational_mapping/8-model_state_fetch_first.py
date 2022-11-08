#!/usr/bin/python3
"""
A script that prints the first State object
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
            @localhost:3306/{sys.argv[3]}")
    Session = sessionmaker(bind=engine)

    session = Session()

    # states = session.query(State).order_by(State.id).all()
    # for state in states:
    #   if "a" in state.name:
    #     print("f{state.id}: {state.name}")
    #  NOTE: This approach is not effective enough as you don't need to query
    # all objects
    # from the database before extracting the first item

    first_state = session.query(State).order_by(State.id).first()
    print(
        "Nothing" if not first_state else "{}: {}".format(
            first_state.id, first_state.name))
