from application import db
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
# class Data(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     notes = db.Column(db.String(128), index=True, unique=False)
    
    # def __init__(self, notes):
    #     self.notes = notes

    # def __repr__(self):
    #     return '<Data %r>' % self.notes
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

	# def __init__(self, name):
	# 	self.name = name

class User(Base):
	__tablename__ = 'user'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(250),nullable=False, unique=False)
	gender = db.Column(db.Boolean)
	age = db.Column(db.Integer)
	# preference = db.Column(db.Binary)
	p1 = db.Column(db.Integer)
	p2 = db.Column(db.Integer)
	p3 = db.Column(db.Integer)
	p4 = db.Column(db.Integer)
	p5 = db.Column(db.Integer)
	p6 = db.Column(db.Integer)
	p7 = db.Column(db.Integer)
	p8 = db.Column(db.Integer)
	p9 = db.Column(db.Integer)
	p10 = db.Column(db.Integer)

	zipCode = db.Column(db.String(250))

	# def __init__(self, name):
	# 	self.name = name

class Mapping(Base):
	__tablename__ = 'mapping'

	source = db.Column(db.String(250), primary_key=True)
	target = db.Column(db.String(250))
	coupon1 = db.Column(db.String(250))
	couple2 = db.Column(db.String(250))
	couple3 = db.Column(db.String(250))
	pending = db.Column(db.Boolean)
	
	# def __init__(self, pending):
	# 	self.pending = pending

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
		# 'preference': self.preference,
		'p1': self.p1,
		'p2': self.p2,
		'p3': self.p3,
		'p4': self.p4,
		'p5': self.p5,
		'p6': self.p6,
		'p7': self.p7,
		'p8': self.p8,
		'p9': self.p9,
		'p10': self.p10,
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
		




