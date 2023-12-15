#!/usr/bin/python3
"""Module Docs"""

import MySQLdb
from sys import argv


def main():
    """Function that takes in an argument and displays all values in
    the states table of hbtn_0e_0_usa where name matches the argument."""

    dbHost = "localhost"
    dbPort = 3306

    db = MySQLdb.connect(host=dbHost, port=dbPort, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    state_name = argv[4]

    cursor.execute(query, (state_name))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
