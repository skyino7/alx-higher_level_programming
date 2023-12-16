#!/usr/bin/python3

"""Module Docs"""

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def main():
    """creates the State “California” with the City “San Francisco”
    from the database hbtn_0e_100_usa: (100-relationship_states_cities.py)"""

    dbUser = argv[1]
    dbPass = argv[2]
    dbName = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(dbUser, dbPass, dbName), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)
    session.add(new_city)
    session.commit()

    session.close()


if __name__ == "__main__":
    main()
