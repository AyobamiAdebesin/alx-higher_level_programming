#!/usr/bin/python3
"""
A script that takes in argument and displays
all values in the states table, but safe from SQL
Injection
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(
            user=sys.argv[1], passwd=sys.argv[2],
            db=sys.argv[3], host="localhost")
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                (argv[4],))
    for i in cur.fetchall():
        print(i)
    db.close()
