#!/usr/bin/python3

"""Module Docs"""

import MySQLdb
from sys import argv


def main():
    """Function that takes in an argument and displays all values in the
    cities table of hbtn_0e_4_usa where name matches the argument"""

    dbHost = "localhost"
    dbPort = 3306

    db = MySQLdb.connect(host=dbHost, port=dbPort, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()

    query = "SELECT cities.name FROM cities INNER JOIN states ON " \
        "cities.state_id = states.id WHERE states.name LIKE %s ORDER BY " \
        "cities.id ASC"
    arg = (argv[4],)

    cursor.execute(query, arg)

    print(", ".join([row[0] for row in cursor.fetchall()]))

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
