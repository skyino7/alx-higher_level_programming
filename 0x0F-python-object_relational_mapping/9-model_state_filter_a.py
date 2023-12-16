#!/usr/bin/python3

"""Module Docs"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv


def main():
    """Function lists all State objects that contain
    the letter a from the database hbtn_0e_6_usa"""

    dbUser = argv[1]
    dbPass = argv[2]
    dbName = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(dbUser, dbPass, dbName), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    qs = (session.query(State).filter(State.name.like
                                      ('%a%')).order_by(State.id).all())

    for state in qs:
        print("{}: {}".format(state.id, state.name))

    session.close()


if __name__ == "__main__":
    main()
