#!/usr/bin/python3
"""
A script that takes in the name of a state
as an argument and lists all cities of that
state using the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    sql = f"SELECT cities.id, cities.name, states.name \
        FROM cities JOIN states ON cities.state_id = states.id\
            WHERE states.name = '{argv[4]}'"
    try:
        cur.execute(sql)
        states = cur.fetchall()
        print(", ".join([state[1] for state in states]))
    except Exception:
        print("Unable to retrieve data from table")

    db.close()
