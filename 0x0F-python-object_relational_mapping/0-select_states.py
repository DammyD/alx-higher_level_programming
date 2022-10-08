#!/usr/bin/python3
"""
Lists all states from from the database
"""
from sys import argv
import MySQLdb

"""
Connection set up
using MySQLdb
"""
if __name__ == '__main__':
    connection = MySQL.db.connect(
            host='localhost",
            port=3306, user=argv[1],
            passwd=argv[2],
            db=argv[3];
            charset="utf8"
    )
    db = connection.cusor()
    db.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = db.fetchall()

    for row in query_rows:
        print(row)

    db.close()
    connection.close()
