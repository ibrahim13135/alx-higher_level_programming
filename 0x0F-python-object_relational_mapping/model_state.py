#!/usr/bin/python3
"""Defines the State class and Base instance"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of the declarative base
Base = declarative_base()


class State(Base):
    """Represents a state for a MySQL database"""

    # Table name
    __tablename__ = 'states'

    # Columns
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        """Returns the string representation of a State instance"""
        return "<State(id='%s', name='%s')>" % (self.id, self.name)
