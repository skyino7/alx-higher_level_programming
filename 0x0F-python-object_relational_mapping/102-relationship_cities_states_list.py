#!/usr/bin/python3

"""Module to list all City objects from
the database hbtn_0e_101_usa"""

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def main():
    """Function to list all City objects from
    the database hbtn_0e_101_usa"""

    dbUser = argv[1]
    dbPass = argv[2]
    dbName = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(dbUser, dbPass, dbName), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.commit()
    session.close()


if __name__ == "__main__":
    main()
