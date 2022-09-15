#!/usr/bin/python3

"""
A script that list all states with a name starting with N
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(
            user=sys.argv[1], passwd=sys.argv[2],
            db=sys.argv[3], host="localhost")
    cur = db.cursor()
    sql = "SELECT * FROM states ORDER BY states.id ASC"
    # Alternatively
    # SELECT * FROM states WHERE states.name LIKE
    # 'N%' ORDER BY states.id ASC
    try:
        cur.execute(sql)
        for result in cur.fetchall():
            if result[1][0] == "N":
                print(result)
    except Exception:
        print("Unable to fetch data from database")
    db.close()
