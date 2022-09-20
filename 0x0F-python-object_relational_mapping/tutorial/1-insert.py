#!/usr/bin/python3
import MySQLdb

db = MySQLdb.connect(db="testdb", host="localhost", user="root", passwd="olaseni1996")
cur = db.cursor()

sql = "INSERT INTO employee(first_name, last_name, age) VALUES ('{}', '{}', {})".format("Ashaolu", "Rose", 23)
try:
    cur.execute(sql)
    db.commit()
except Exception:
    raise ValueError("Unable to insert data into table")
    db.rollback()

db.close()