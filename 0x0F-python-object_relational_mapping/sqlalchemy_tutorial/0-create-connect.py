#!/usr/bin/python3
import sqlalchemy
from sqlalchemy import create_engine
engine = create_engine("mysql+mysqldb://root:olaseni1996@localhost/testdb")
engine.connect()
print(engine)

