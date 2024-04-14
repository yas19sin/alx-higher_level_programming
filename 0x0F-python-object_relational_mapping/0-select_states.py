#!/usr/bin/python3
"""Select all states from the database hbtn_0e_0_usa and print them."""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
