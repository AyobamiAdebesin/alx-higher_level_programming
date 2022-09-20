#!/usr/bin/python3
"""
A script that prints all City objects
from the database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City, State

if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}://@\
        localhost:3306/{sys.argv[3]}")
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_city = session.query(State, City).filter(State.id == City.state_id).all()
    for state, city in state_city:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
