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

    new_state = State()
    new_state.name = "Ogun"

    session.add(new_state)
    session.commit()
    print(new_state.id)
