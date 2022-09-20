#!/usr/bin/python3
import MySQLdb

db = MySQLdb.connect(user="root", passwd="olaseni1996", db="testdb", host="localhost")
cur = db.cursor()

sql = "DROP TABLE IF EXISTS employee"
cur.execute(sql)

sql = """CREATE TABLE IF NOT EXISTS employee(
    first_name VARCHAR(256) NOT NULL,
    last_name VARCHAR(256) NOT NULL,
    age INT
    )"""

cur.execute(sql)

db.close()
