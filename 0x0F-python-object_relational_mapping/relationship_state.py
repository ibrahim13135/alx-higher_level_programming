#!/usr/bin/python3
"""Defines the State class"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """Represents a state for a MySQL database"""

    __tablename__ = 'states'

    # Columns
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")

    def __repr__(self):
        """Returns the string representation of a State instance"""
        return "<State(id='%s', name='%s')>" % (self.id, self.name)
