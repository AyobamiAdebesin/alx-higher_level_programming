#!/usr/bin/python3

import sqlalchemy
import os, sys
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine

#dialect+driver://username:password@localhost:port/database

if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
            @localhost:3306/{sys.argv[3]}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Random State")
    new_city = City(name="Random City")

    new_state.cities.append(new_city)

    session.add(new_state)
    session.add(new_city)
    session.commit()
