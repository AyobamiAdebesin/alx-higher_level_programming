#!/usr/bin/python3
import MySQLdb

db = MySQLdb.connect(db="testdb", host="localhost", user="root", passwd="olaseni1996")
cur = db.cursor()

sql = "UPDATE employee SET age = 18 WHERE first_name = 'Ashaolu'"

try:
    cur.execute(sql)
    db.commit()
except:
    print("Unable to update data in the table")
    db.rollback()
db.close()