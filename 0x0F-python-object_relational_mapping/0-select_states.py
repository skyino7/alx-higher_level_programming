#!/usr/bin/python3
"""Module Docs"""

import MySQLdb
from sys import argv

def main():
    """Function that lists all states from the database hbtn_0e_0_usa"""

    dbHost = "localhost"
    dbPort = 3306

    db = MySQLdb.connect(host=dbHost, port=dbPort, user=argv[1], passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
