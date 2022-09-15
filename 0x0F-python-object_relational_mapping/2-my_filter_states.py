#!/usr/bin/python3

"""
A script that takes in argument and displays
all values in the states table
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(
            user=sys.argv[1], passwd=sys.argv[2],
            db=sys.argv[3], host="localhost")
    cur = db.cursor()

    sql = "SELECT * FROM states WHERE states.name='{}'".format(sys.argv[4])
    cur.execute(sql)
    for result in cur.fetchall():
        if result[1] == sys.argv[4]:
            print(result)
    db.close()
