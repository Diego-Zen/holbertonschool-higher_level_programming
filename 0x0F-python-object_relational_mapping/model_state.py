#!/usr/bin/python3
"""
    Define a state model module
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """ defines a state

    Attr:
    id (int): unique identifier
    name (str): states name
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        self.name = name
