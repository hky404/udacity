import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base() # will create tables in the DB based on python classes

# 'Restaurant' will be the name of the table in DB.
class Restaurant(Base):
	__tablename__ = 'restaurant'

	# 'name' which is a python object will be a column in DB.
	name = Column(String(80), nullable = False) # map python objects to columns in our database
	id = Column(Integer, primary_key = True)

class MenuItem(Base):
	__tablename__ = 'menu_item'

	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
	course = Column(String(250))
	description = Column(String(250))
	price = Column(String(8))
	restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
	restaurant = relationship(Restaurant)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine) # will go in the DB and will create the tables based on python classes.
