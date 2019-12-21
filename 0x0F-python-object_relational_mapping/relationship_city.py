#!/usr/bin/python3
"""
    Define a city model module
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_state import Base, State


class City(Base):
    """ defines a city

    Attr:
    id (int): unique identifier
    name (str): city name
    state_id (int): state id
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
