#!/usr/bin/python3
"""Module Docs"""

import MySQLdb
from sys import argv


def main():
    """Function that lists all states with a name starting with N
    (upper N) from the database hbtn_0e_0_usa"""

    dbHost = "localhost"
    dbPort = 3306

    db = MySQLdb.connect(host=dbHost, port=dbPort, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()

    q = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"

    cursor.execute(q)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
