#!/usr/bin/python3

"""
A script that list all states from a database
Usage: ./0-select_states.py <mysql_username> <mysql-password> <mysql-db>
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(
            user=sys.argv[0], passwd=sys.argv[1],
            db=sys .argv[2], host="localhost")
    cur = db.cursor()

    sql = " SELECT * FROM states ORDER BY states.id ASC"
    try:
        cur.execute(sql)
        results = db.fetchall()
        for result in results:
            print(result)
    except Exception:
        print("Unable to fetch data from database")
    db.close()
