from application import db
from application.models import Restaurant, User, Mapping
import os
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()

# db.create_all()
class Restaurant(Base):
	__tablename__ = 'restaurant'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(250), nullable=False, unique=False)
	category = db.Column(db.Integer)
	pic1 = db.Column(db.String(250))
	pic2 = db.Column(db.String(250))
	pic3 = db.Column(db.String(250))
	coupon = db.Column(db.String(250))
	zipCode = db.Column(db.String(250))

class User(Base):
	__tablename__ = 'user'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(250),nullable=False, unique=False)
	preference = db.Column(db.Integer)
	image=db.Column(db.String(250))
	gender=db.Column(db.String(250))
	age=db.Column(db.Integer)
	email=db.Column(db.String(250))

class Mapping(Base):
	__tablename__ = 'mapping'
    
	id = db.Column(db.Integer, primary_key=True)
	source = db.Column(db.String(250),nullable=False, unique=False)
	target = db.Column(db.String(250),nullable=False)
	coupon1 = db.Column(db.String(250))
	couple2 = db.Column(db.String(250))
	couple3 = db.Column(db.String(250))
	pending = db.Column(db.Integer)
	used = db.Column(db.Integer)
@property
def serializeRestaurant(self):
	return {
		'id': self.id,
		'name': self.name,
		'category': self.category,
		'pic1': self.pic1,
		'pic2': self.pic2,
		'pic3': self.pic3,
		'coupon': self.coupon,
		'zipCode': self.zipCode
	}

@property
def serializeUser(self):
	return {
		'id': self.id,
		'name': self.name,
		'gender': self.gender,
		'age': self.age,
		'preference': self.preference,
		'zipCode': self.zipCode
	}

@property
def serializeMapping(self):
	return {
		'source': self.source,
		'target': self.target,
		'coupon1': self.coupon1,
		'coupon2': self.coupon2,
		'coupon3': self.coupon3,
		'pending': self.pending
	}

engine = create_engine('sqlite:///test.db')
Base.metadata.create_all(engine)

print("DB created.")
