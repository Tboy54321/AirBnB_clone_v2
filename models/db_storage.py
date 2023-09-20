#!/usr/bin/python3
"""This module defines the engine for the MySQL database"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Constructor for DBStorage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_PORT'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

        # Create a new session for this instance
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                      expire_on_commit=False))
    
    def all(self, cls=None):
        """Query objects from the current database session."""
        query_objects = []

        if cls:
            # Query objects based on the specified class
            query_objects.extend(self.__session.query(cls).all())
        else:
            # Query all types of objects
            classes = [State, City, User, Amenity, Place, Review]
            for cls in classes:
                query_objects.extend(self.__session.query(cls).all())

        # Create a dictionary with the format <class-name>.<object-id>: object
        result_dict = {f"{type(obj).__name__}.{obj.id}": obj for obj in query_objects}

        return result_dict
    
    def new(self, obj):
        """Add the object to the current database session."""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None."""
        if obj:
            self.__session.delete(obj)
    
    def reload(self):
        """Create all tables in the database and set up the current database session."""
        Base.metadata.create_all(self.__engine)

        # Create a new session for this instance with options
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
    
    def close(self):
        """public method to call remove method"""
        DBStorage.__session.close()