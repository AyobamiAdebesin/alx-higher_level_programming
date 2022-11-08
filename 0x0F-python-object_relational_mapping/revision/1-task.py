#!/usr/bin/python3

if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(
        host="localhost", user=sys.argv[1], 
        passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    sql = "SELECT * FROM states ORDER BY states.id ASC"

    try:
        cur.execute(sql)
        results = cur.fetchall()
        for row in results:
            if row[1][0] == "N":
                print(row)
    except Exception as e:
        print("Unable to read data")
    db.close()
