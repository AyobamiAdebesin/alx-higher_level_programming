#!/usr/bin/python3
import MySQLdb

db = MySQLdb.connect(db="testdb", host="localhost", user="root", passwd="olaseni1996")
cur = db.cursor()

sql = "DELETE FROM employee WHERE AGE = 18"
try:
    cur.execute(sql)
    db.commit()
except Exception:
    raise ValueError("Unable to delete data from table")
    db.rollback()

db.close()
