#!/usr/bin/python3

"""Module Docs"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):

    """Class definition of a City"""

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # state = relationship("State", back_populates="cities")
