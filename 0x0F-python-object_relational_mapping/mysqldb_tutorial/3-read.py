#!/usr/bin/python3
import MySQLdb

db = MySQLdb.connect(db="testdb", host="localhost", user="root", passwd="olaseni1996")
cur = db.cursor()

sql = "SELECT * FROM employee"

try:
    cur.execute(sql)
    results = cur.fetchall()
    for row in results:
        print(f"First Name: {row[0]}, Last Name: {row[1]}, Age: {row[2]}")

except Exception:
    print("Unable to retrieve data")
db.close()