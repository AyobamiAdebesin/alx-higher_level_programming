#!/usr/bin/python3

import sqlalchemy
import os, sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine

#dialect+driver://username:password@localhost:port/database

if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
            @localhost:3306/{sys.argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()

    st_cty = session.query(State, City).filter(State.id == City.state_id).all()
    
    for i in range(len(st_cty)):
        st = st_cty[i][0]
        cty = st_cty[i][1]

        print(f"{st.name}: ({st.id}) {cty.name}")
