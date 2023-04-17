#!/usr/bin/python3
"""
Python script listing all states starting with N from a database hbtn_0e_0_usa
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

    # executing MYSQL query to list all states
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' \
            ORDER BY states.id ASC")

    # fetch and print out each data row from the database
    rows = cursor.fetchall()
    for row_s in rows:
        print(row_s)

    # closing connection
    cursor.close()
    db.close()
