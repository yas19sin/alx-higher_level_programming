#!/usr/bin/python3
"""Script to safely filter the states in the database hbtn_0e_0_usa
 and print them."""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    cursor = db.cursor()
    state_name = MySQLdb.escape_string(sys.argv[4])

    cursor.execute("""SELECT * FROM states WHERE name = %s
                    ORDER BY states.id ASC""", (state_name,))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
