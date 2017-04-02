from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_create import Restaurant, User, Mapping, Base

engine = create_engine('sqlite:///test.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()
# add restaurants

# category 1: Chinese Restaurant
restaurant1 = Restaurant(name="Hsus Atlanta", category=1, 
	pic1='https://eat24-files-live.s3.amazonaws.com/cuisines/v4/chinese.jpg?Signature=Wqq5KFt%2Fu13sshe4dcjJE1fsPYk%3D&Expires=1489974731&AWSAccessKeyId=AKIAIEJ2GCCJRT63TBYA',
	pic2='https://s-media-cache-ak0.pinimg.com/736x/3d/6e/6f/3d6e6ffdce7cfed1028a6959a8527b2c.jpg', 
	pic3='http://www.chongschineserestaurant.com/24-noodles.jpg', 
	coupon='coupon here!', zipCode='30303')
session.add(restaurant1)
session.commit()