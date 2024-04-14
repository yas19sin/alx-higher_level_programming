#!/usr/bin/python3
"""Filter cities by state name and print them."""
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
    cursor.execute("""
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (state_name,))

    cities = [row[0] for row in cursor.fetchall()]

    print(", ".join(cities))

    cursor.close()
    db.close()
