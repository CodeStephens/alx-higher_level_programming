#!/usr/bin/python3
"""
Python script lists all cities from the database
--> usage: ./4-cities_by_state.py root root hbtn_0e_4_usa `args`
                where `args` is the state name for which list is to provided
"""


# import needed module for the functionality of the script's purpose
import MySQLdb
from sys import argv

# establishing a database connection
if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])

    # name of state whose list of cities is being sought for
    stateName = argv[4]

    # creating an environment for implementation of database queries
    cursor = db.cursor()

    # executing MYSQL query to list all cities in ascending order of cities.id
    # using parameterized query to fend off SQL injection
    cursor.execute("SELECT cities.name FROM cities\
            INNER JOIN states ON states.id = cities.state_id\
            WHERE states.name = %s\
            ORDER BY cities.id ASC", (stateName,))

    # fetch and print out each data row from the database
    rows = cursor.fetchall()
    for row_s in rows:
        print(row_s[0], end=", " if row_s != rows[-1] else "\n")

    # closing connection
    cursor.close()
    db.close()
