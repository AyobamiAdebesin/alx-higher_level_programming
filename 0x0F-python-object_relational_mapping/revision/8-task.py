#!/usr/bin/python3

import sqlalchemy
import os, sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine

#dialect+driver://username:password@localhost:port/database

if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
            @localhost:3306/{sys.argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    if len(states) == 0:
        print("Nothing")
    else:
        print(f"{states[0].id}: {states[0].name}")
