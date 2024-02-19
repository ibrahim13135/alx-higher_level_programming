#!/usr/bin/python3
"""Defines the City class"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """Represents a city for a MySQL database"""

    # Table name
    __tablename__ = 'cities'

    # Columns
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __repr__(self):
        """Returns the string representation of a City instance"""
        return "<City(id='%s', name='%s', state_id='%s')>" % (self.id, self.name, self.state_id)
