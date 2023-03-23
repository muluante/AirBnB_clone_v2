#!/usr/bin/python3
""" State Module for HBNB project """
import models
from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="delete, merge, save-update")

    if getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def cities(self):
            """Returns the list of Citys with state_id = State.id"""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
