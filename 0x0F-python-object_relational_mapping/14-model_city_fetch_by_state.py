#!/usr/bin/python3

"""Module Docs"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sys import argv


def main():
    """Function prints all City objects from the database hbtn_0e_14_usa"""

    dbUser = argv[1]
    dbPass = argv[2]
    dbName = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(dbUser, dbPass, dbName), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state, city in session.query(State, City).\
            join(City, State.id == City.state_id).order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()


if __name__ == "__main__":
    main()
