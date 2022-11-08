#!/usr/bin/python3
"""
A script that list all cities from the database
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()

    sql = "SELECT cities.id, cities.name, states.name FROM cities\
        JOIN states ON cities.state_id=states.id"
    cur.execute(sql)
    for city in cur.fetchall():
        print(city)
    db.close()
