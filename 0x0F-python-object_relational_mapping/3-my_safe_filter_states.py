#!/usr/bin/python3
"""
A script that takes in argument and displays
all values in the states table, but safe from SQL
Injection
"""

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                (argv[4],))

    for state in cur.fetchall():
        print(state)

    db.close()
