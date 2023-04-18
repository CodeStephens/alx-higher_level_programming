#!/usr/bin/python3
"""
Python script lists all cities from the database
--> usage: ./4-cities_by_state.py root root hbtn_0e_4_usa
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

    # creating an environment for implementation of database queries
    cursor = db.cursor()

    # executing MYSQL query to list all cities in ascending order of cities.id
    cursor.execute("SELECT cities.id, cities.name, states.name\
            FROM cities INNER JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC")

    # fetch and print out each data row from the database
    rows = cursor.fetchall()
    for row_s in rows:
        print(row_s)

    # closing connection
    cursor.close()
    db.close()
