#!/usr/bin/python3

"""Module Docs"""
import MySQLdb
from sys import argv


def main():
    """Function that takes in an arguments and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument. But
    this time, write one that is safe from MySQL injections"""

    dbHost = "localhost"
    dbPort = 3306

    db = MySQLdb.connect(host=dbHost, port=dbPort, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    arg = (argv[4],)

    cursor.execute(query, arg)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
