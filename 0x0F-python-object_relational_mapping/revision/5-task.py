#!/usr/bin/python3
"""
A script that list all cities from the database
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    sql = "SELECT cities.id, cities.name, states.name FROM cities\
        JOIN states ON cities.state_id=states.id WHERE states.name = '{}' ".format(sys.argv[4])
    cur.execute(sql)
    for city in cur.fetchall():
        print(city)
    db.close()
