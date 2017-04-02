# Uncomment the line below if you want to work with a local DB
#SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://FoodLink:FoodLink@foodlink.cgp8ptgymxq4.us-west-2.rds.amazonaws.com:3306/FoodLink'
SQLALCHEMY_DATABASE_URI = 'sqlite:////test.db'
SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True