from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_create import Restaurant, User, Mapping, Base

engine = create_engine('sqlite:///test.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# user3=User(name='Candy', preference=0,image='http://your-insurer.com/wp-content/uploads/2015/01/Agent-Sing2.jpg')
# session.add(user3)
# session.commit()

# user4=User(name='David', preference=0,image='https://userscontent2.emaze.com/images/ef511f5d-96fa-4e7e-a7e1-49db36a8e9a2/715509f9d4ef6b01e018135121a72623.jpg')
# session.add(user4)
# session.commit()

# user5=User(name='Eric',preference=0,image='http://www.tonydczech.com/Tony_Cartoon.jpg')
# session.add(user5)
# session.commit()

# user6=User(name='Frank', preference=0,image='https://s-media-cache-ak0.pinimg.com/236x/df/4a/bd/df4abd207e53c233928a67e0ce2c71ee.jpg')
# session.add(user6)
# session.commit()

# user7=User(name='George', preference=0,image='https://s-media-cache-ak0.pinimg.com/originals/2b/91/e7/2b91e763053b29f2b4995f901de34417.jpg')
# session.add(user7)
# session.commit()

# user8=User(name='Hebe', preference=0,image='http://kastorskorner.com/wp/wp-content/uploads/2015/06/BUBBLES_01_PR-265x300.jpg')
# session.add(user8)
# session.commit()

# user9=User(name='Iris', preference=0,image='https://s-media-cache-ak0.pinimg.com/736x/4b/53/55/4b53554766a2ed8fe948c08b09f37b1b.jpg')
# session.add(user9)
# session.commit()

# user10=User(name='Jason', preference=0,image='http://comedycentral.mtvnimages.com/images/show_images/TVE_Hub_ShowImage_DrawnTogether.jpg?')
# session.add(user10)
# session.commit()

# user1=User(name='Mary', preference=0,image='http://www.counsellingathome.com/wp-content/uploads/2015/07/Adrian-Holmes-Cartoon-Profile.jpg')
# session.add(user1)
# session.commit()

user = session.query(User).filter_by(name='Bob').one()
user.image = "http://yuer.coorank.com/files/i_d/282/thumbnail/288943_081046.jpeg"
session.commit()



