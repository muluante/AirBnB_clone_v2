#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """This class manages storage of hbnb models in database"""
    __engine = None
    __session = None

    def __init__(self):
        """Create a db engine"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
                                      getenv("HBNB_MYSQL_USER"),
                                      getenv("HBNB_MYSQL_PWD"),
                                      getenv("HBNB_MYSQL_HOST"),
                                      getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query on current database session all objects
        depending of the class name (argument cls)
        """
        dictionary = {}
        if cls is not None:
            objs = self.__engine.query(cls)
            for o in objs:
                key = "{}.{}".format(type(o).__name__, o.id)
                dictionary[key] = o
            return dictionary
        else:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        ses = sessionmaker(bind=self.__engine,
                           expire_on_commit=False)
        Session = scoped_session(ses)
        self.__session = Session()
