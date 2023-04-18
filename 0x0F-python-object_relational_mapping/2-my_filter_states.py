#!/usr/bin/python3
"""
Python script listing states correspodnding to a state searched keyword
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

    # keyword to be searched for
    searchedWord = argv[4]

    # creating an environment for implementation of database queries
    cursor = db.cursor()

    # executing MYSQL query to list all states
    cursor.execute("SELECT * FROM states\
            WHERE name LIKE BINARY '{}' \
            ORDER BY states.id ASC".format(searchedWord))

    # fetch and print out each data row from the database
    rows = cursor.fetchall()
    for row_s in rows:
        print(row_s)

    # closing connection
    cursor.close()
    db.close()
