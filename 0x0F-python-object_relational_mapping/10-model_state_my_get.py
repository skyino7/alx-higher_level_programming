#!/usr/bin/python3

"""Module Docs"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv


def main():
    """Function that prints the State object with the name passed as argument
    from the database hbtn_0e_6_usa"""

    dbUser = argv[1]
    dbPass = argv[2]
    dbName = argv[3]
    stateName = argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(dbUser, dbPass, dbName), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    qs = (session.query(State).filter(State.name == stateName)
          .order_by(State.id).all())

    if qs:
        print(qs[0].id)
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":
    main()
