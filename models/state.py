#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    cities = relationship("City",
                          backref="state",
                          cascade="all, delete-orphan",
                          passive_deletes=True)

    if environ.get('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            return [city for city in models.storage.all(
                City).values() if city.state_id == self.id]
