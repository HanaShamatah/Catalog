# configuration code__beginning
import os
import sys
from sqlalchemy import (Column,
                        ForeignKey,
                        Integer,
                        String,
                        DateTime)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

# In order to create a base class that our class code will inherit
Base = declarative_base()


class User(Base):
    """
    Logged in users information will be stored in user table in db
    """
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)  # Mapper code
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

    @property
    def serialize(self):
        # Return object data in easily serializeable format
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'picture': self.picture,
        }


class Categories(Base):  # Class code
    """
    Main categories will be stored in categories table in db
    """
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)  # Mapper code
    name = Column(String(250), unique=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User")

    @property
    def serialize(self):
        # Return object data in easily serializeable format
        return {
            'name': self.name,
            'id': self.id,
        }


class CatalogItem(Base):  # Class code
    """
    Items of categories will be stored in catalog_item table in db
    """
    __tablename__ = 'catalog_item'

    name = Column(String(80), nullable=False)  # Mapper code
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    description = Column(String(250))
    picture = Column(String(250))
    category_name = Column(String(250), ForeignKey('categories.name'))
    categories = relationship("Categories", backref=backref("catalog_item", cascade="all, delete, save-update"))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User")

    @property
    def serialize(self):
        # Return object data in easily serializeable format
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'picture': self.picture,
        }


# configuration code__end
engine = create_engine('postgresql://catalog:catalog@localhost/catalog')


Base.metadata.create_all(engine)
