from flask import Flask, render_template, request, redirect, url_for, jsonify,flash
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_create import Restaurant, User, Mapping, Base
import random
from sqlalchemy.orm import scoped_session
application = Flask(__name__)
application.debug = True
application.secret_key = 'cC1YCIWOj9GgWspgNEo2'

engine = create_engine('sqlite:///test.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = scoped_session(DBSession)
#session = DBSession()
#session._model_changes = {}

@application.teardown_request
def remove_session(ex=None):
    session.remove()

# main page
@application.route('/')
def Mainpage():
    return render_template('login.html')

@application.route('/login/', methods=['POST'])
def Login():
    name = request.form['name']
    gender = request.form['gender']
    picture = request.form['picture']
    email = request.form['email']
    age = request.form['age']
    user = session.query(User).filter_by(name=name).all()
    if len(user) == 0:
        newuser = User(name=name, preference=0, image=picture, gender=gender, age=age, email=email)
        session.add(newuser)
        session.commit()
    else:
        user[0].name=name
        user[0].image=picture
        user[0].age=age
        user[0].gender=gender
        user[0].email=email
        print 'here'
        session.commit()
    return redirect(url_for('StartPage', user_name=name))

@application.route('/<string:user_name>/', methods=['GET'])
def StartPage(user_name):
    return render_template('welcomepage.html', user_name=user_name)

@application.route('/showtime', methods=['GET', 'POST'])
def showtime():
    return render_template('product_website.html')
@application.route('/gp/<string:user_name>',methods=['GET','POST'])
#def givePicture(user_name):
#    if request.method=='GET':
#        restaurants = session.query(Restaurant).all()
#        restIndex = random.sample(range(0,9), 5)
#        resIndex2 = random.sample(range(0,9), 5)
#        # print restIndex
#        Restaurants=[]
#        images=[]
#        prefer=[]
#        for i in range(0,5):
#            Restaurants.append(restaurants[restIndex[i]*10+resIndex2[i]])
#            index=random.randint(1,3)
#            prefer.append(restaurants[restIndex[i]*10+resIndex2[i]].category)
#            if index == 1:
#                images.append(restaurants[restIndex[i]*10+resIndex2[i]].pic1)
#            if index == 2:
#                images.append(restaurants[restIndex[i]*10+resIndex2[i]].pic2)
#            if index == 3:
#                images.append(restaurants[restIndex[i]*10+resIndex2[i]].pic3)
#        # print restIndex, prefer
#        print images
#        return render_template('imageslide.html', user_name=user_name, Restaurants=Restaurants, images=images,prefer=prefer,count=5)
@application.route('/gp/<string:user_name>',methods=['GET','POST'])
def givePicture(user_name):
    if request.method=='GET':
        restaurants = session.query(Restaurant).all()
        restIndex = random.sample(range(0,9), 5)
        resIndex2 = random.sample(range(0,9), 5)
        # print restIndex
        Restaurants=[]
        images=[]
        prefer=[]
        for i in range(0,5):
            Restaurants.append(restaurants[restIndex[i]*10+resIndex2[i]])
            index=random.randint(1,3)
            prefer.append(restaurants[restIndex[i]*10+resIndex2[i]].category)
            if index == 1:
                images.append(restaurants[restIndex[i]*10+resIndex2[i]].pic1)
            if index == 2:
                images.append(restaurants[restIndex[i]*10+resIndex2[i]].pic2)
            if index == 3:
                images.append(restaurants[restIndex[i]*10+resIndex2[i]].pic3)
        # print restIndex, prefer
        return render_template('imageslide.html', user_name=user_name, Restaurants=Restaurants, images=images,prefer=prefer,count=5)

@application.route('/update/<string:user_name>',methods=['POST'])
def update_preference(user_name):
    user = session.query(User).filter_by(name=user_name).one()
    pre0=int(request.form['pre0'])
    pre1=int(request.form['pre1'])
    pre2=int(request.form['pre2'])
    pre3=int(request.form['pre3'])
    pre4=int(request.form['pre4'])
    # print(pre4)
    # print(pre3)
    # print(pre2)
    # print(pre1)
    # print(pre0)
    if pre0>0:
        user.preference = user.preference | pow(2, pre0-1)
    else:
        user.preference = user.preference & (1023-pow(2, -pre0-1))
    
    session.commit()
    if pre1>0:
        user.preference = user.preference | pow(2, pre1-1)
    else:
        user.preference = user.preference & (1023-pow(2, -pre1-1))
    session.commit()

    if pre2>0:
        user.preference = user.preference | pow(2, pre2-1)
    else:
        user.preference = user.preference & (1023-pow(2, -pre2-1))
    session.commit()

    if pre3>0:
        user.preference = user.preference | pow(2, pre3-1)
    else:
        user.preference = user.preference & (1023-pow(2, -pre3-1))
    session.commit()

    if pre4>0:
        user.preference = user.preference | pow(2, pre4-1)
    else:
        user.preference = user.preference & (1023-pow(2, -pre4-1))
    
    session.commit()
    friAndPending = []
    candidates = []
    mapping1 = session.query(Mapping).filter_by(source=user_name).all()
    mapping2 = session.query(Mapping).filter_by(target=user_name).all()
    
    for mapping in mapping1:
        
        if mapping.target not in friAndPending:
            friAndPending.append(mapping.target)
    for mapping in mapping2:
        if mapping.source not in friAndPending:
            friAndPending.append(mapping.source) 
    friAndPending.append(user_name)
    users = session.query(User).all()
    for _user in users:
        if _user.name not in friAndPending:
            candidates.append(_user)
    friendID = 0
    matched = 0
    for candidate in candidates:
        likeCnt = 0
        mask = 0x1
        prefVector = candidate.preference & user.preference
        for i in range(0,10):
            if mask & prefVector != 0:
                likeCnt += 1
            mask = mask << 1
        if likeCnt < 4:
            continue
        prefVector = 1023 - candidate.preference ^ user.preference
        preCnt = 0
        mask = 0x1
        for i in range(0, 10):
            digit = mask & prefVector
            mask = mask << 1
            if digit != 0:
                preCnt += 1
            if preCnt >= 5:
                matched = 1
                friendID = candidate.id
                break
        if matched == 1:
            break
    matched = 1
    friendID = 1
    if matched == 1:
        target = session.query(User).filter_by(id=friendID).one()
        mask = 0x1
        cat = 0
        for i in range(1,11):
            if mask & target.preference > 0:
                cat = i
                break
            mask = mask << 1
        if cat == 1:
            mask = 'Chinese Food'
        if cat == 2:
            mask = 'Indian Food'
        if cat == 3:
            mask = 'Mexico Food'
        if cat == 4:
            mask = 'French Food'
        if cat == 5:
            mask = 'Cafe'
        if cat == 6:
            mask = 'Spanish Food'
        if cat == 7:
            mask = 'American Food'
        if cat == 8:
            mask = 'Italian Food'
        if cat == 9:
            mask = 'Japanese Food'
        if cat == 10:
            mask = 'Korean Food'
        return render_template('friend_card.html', user_name=user_name, target=target, food=mask)
    else:
        return redirect(url_for('givePicture', user_name=user_name))



@application.route('/deal_friend/<string:user_name>/<string:friend_name>',methods=['POST','GET'])
def deal_friend(user_name,friend_name):
    agree=request.form['agree']
    user = session.query(User).filter_by(name=user_name).one()
    target=session.query(User).filter_by(name=friend_name).one()
    if agree=="agree":
        res = restaurants = session.query(Restaurant).all()
        # index=random.randint(0,len(res)-1)
        prefVector = user.preference & target.preference
        # print prefVector
        categoryIndex = []
        mask = 0x1
        for i in range(1,11):
            if prefVector & mask != 0:
                categoryIndex.append(i)
            mask = mask << 1
        length = 3 if len(categoryIndex) >=3 else len(categoryIndex)
        couponIndex = random.sample(categoryIndex, length)
        newmap=Mapping(source=user_name,target=friend_name, pending=1, used=0)
        couponRandom = random.randint(0,9)
        if length == 0:
            newmap.coupon1 = restaurants[random.randint(0,len(restaurants))].name
        if length == 1:
            newmap.coupon1 = restaurants[(couponIndex[0]-1)*10+couponRandom].name
        if length == 2:
            newmap.coupon1 = restaurants[(couponIndex[0]-1)*10+couponRandom].name
            newmap.couple2 = restaurants[(couponIndex[1]-1)*10+couponRandom].name
        if length >=3:
            newmap.coupon1 = restaurants[(couponIndex[0]-1)*10+couponRandom].name
            print newmap.coupon1
            newmap.couple2 = restaurants[(couponIndex[1]-1)*10+couponRandom].name
            print newmap.couple2
            newmap.couple3 = restaurants[(couponIndex[2]-1)*10+couponRandom].name
            print newmap.couple3
        session.add(newmap)
        session.commit()
        return redirect(url_for('givePicture', user_name=user_name))
    else:
        return redirect(url_for('givePicture', user_name=user_name))

@application.route('/add_friend/<string:user_name>/<string:friend_name>')
def add_friend(user_name,friend_name):
    mapping=session.query(Mapping).filter_by(source=friend_name,target=user_name).one()
    mapping.pending=0
    session.commit()
    return redirect(url_for('getFriend',user_name=user_name))

@application.route('/deny_friend/<string:user_name>/<string:friend_name>')
def deny_friend(user_name,friend_name):
    mapping=session.query(Mapping).filter_by(source=friend_name,target=user_name).first()
    session.delete(mapping)
    session.commit()
    return redirect(url_for('getFriend',user_name=user_name))


@application.route('/friend/<string:user_name>',methods=['POST','GET'])
def getFriend(user_name):
    mapping1=session.query(Mapping).filter_by(source=user_name).all()
    mapping2=session.query(Mapping).filter_by(target=user_name).all()
    res=[]
    pend=[]
    for i in range(0,len(mapping1)):
        if mapping1[i].pending==0:
            user = session.query(User).filter_by(name=mapping1[i].target).one()
            res.append(user)
    for i in range(0,len(mapping2)):
        user = session.query(User).filter_by(name=mapping2[i].source).one()
        if mapping2[i].pending==0:
            res.append(user)
        else:
            pend.append(user)
    return render_template("friends.html",friendlist=res,pendlist=pend,user_name=user_name)



@application.route('/friend_profile/<string:user_name>',methods=['POST','GET'])
def getFriendProfile(user_name):
    friend=request.form['friend']
    user=session.query(User).filter_by(name=friend).one()
    return render_template("profile.html",user=user,user_name=user_name)



@application.route('/profile/<string:user_name>',methods=['POST','GET'])
def getSelfProfile(user_name):
    user=session.query(User).filter_by(name=user_name).one()
    return render_template("profile.html",user=user,user_name=user_name)

@application.route('/coupon/<string:user_name>',methods=['POST','GET'])
def getCoupon(user_name):
    mapping1=session.query(Mapping).filter_by(source=user_name).all()
    mapping2=session.query(Mapping).filter_by(target=user_name).all()
    res=[]
    for i in range (0,len(mapping1)):
        if(mapping1[i].pending==0):
            # print mapping1[i].coupon1
            # Rec=session.query(Restaurant).filter_by(name=mapping1[i].coupon1).one()
            if mapping1[i].coupon1 != None:
                Rec = session.query(Restaurant).filter_by(name=mapping1[i].coupon1).first()
                res.append({'friend':mapping1[i].target,'rec':Rec})
            if mapping1[i].couple2 != None:
                Rec = session.query(Restaurant).filter_by(name=mapping1[i].couple2).first()
                res.append({'friend':mapping1[i].target,'rec':Rec})
            if mapping1[i].couple3 != None:
                Rec = session.query(Restaurant).filter_by(name=mapping1[i].couple3).first()
                res.append({'friend':mapping1[i].target,'rec':Rec})

    for i in range (0,len(mapping2)):
        if(mapping2[i].pending==0):
            if mapping2[i].coupon1 != None:
                # print mapping2[i].coupon1
                Rec = session.query(Restaurant).filter_by(name=mapping2[i].coupon1).first()
                res.append({'friend':mapping2[i].source,'rec':Rec})
            if mapping2[i].couple2 != None:
                Rec = session.query(Restaurant).filter_by(name=mapping2[i].couple2).first()
                res.append({'friend':mapping2[i].source,'rec':Rec})
            if mapping2[i].couple3 != None:
                Rec = session.query(Restaurant).filter_by(name=mapping2[i].couple3).first()
                res.append({'friend':mapping2[i].source,'rec':Rec})
    # print res
    return render_template("coupons.html",rec_set=res,user_name=user_name)

@application.route('/deal_coupon/<string:user_name>/<string:friend_name>', methods=['POST','GET'])
def deal_coupon(user_name, friend_name):
    rec = request.form['rec']
    print rec
    # rec = session.query(Restaurant).filter_by(name=rec).first()
    mapping1 = session.query(Mapping).filter_by(source=user_name, target=friend_name).first()
    mapping2 = session.query(Mapping).filter_by(source=friend_name, target=user_name).first()
    if mapping1 != None:
        if rec == mapping1.coupon1:
            mapping1.used = mapping1.used | 32
            session.commit()
            if mapping1.used & 16 != 0:
                flash("Now you can have meal with friends using coupon!")
                mapping1.coupon1 = None
                mapping1.used = mapping1.used & 15
                session.commit()
        if rec == mapping1.couple2:
            mapping1.used = mapping1.used | 8
            session.commit()
            if mapping1.used & 4 != 0:
                flash("Now you can have meal with friends using coupon!")
                mapping1.couple2 = None
                mapping1.used = mapping1.used & 51
                session.commit()
        if rec == mapping1.couple3:
            mapping1.used = mapping1.used | 2
            session.commit()
            if mapping1.used & 1 != 0:
                flash("Now you can have meal with friends using coupon!")
                mapping1.couple3 = None
                mapping1.used = mapping1.used & 60
                session.commit()
    if mapping2 != None:
        if rec == mapping2.coupon1:
            print "here"
            mapping2.used = mapping2.used | 16
            session.commit()
            flash("Now you can wait for your friends to use coupon!")
            # temp = session.query(Mapping).filter_by(source=friend_name, target=user_name).first()
            # print temp.used
            if mapping2.used & 32 != 0:
                flash("Now you can have meal with friends using coupon!")
                mapping2.coupon1 = None
                mapping2.used = mapping2.used & 15
                session.commit()
        if rec == mapping2.couple2:
            mapping2.used = mapping2.used | 4
            session.commit()
            if mapping2.used & 8 != 0:
                flash("Now you can have meal with friends using coupon!")
                mapping2.couple2 = None
                mapping2.used = mapping2.used & 51
                session.commit()
        if rec == mapping2.couple3:
            mapping2.used = mapping2.used | 1
            session.commit()
            if mapping2.used & 2 != 0:
                flash("Now you can have meal with friends using coupon!")
                mapping2.couple3 = None
                mapping2.used = mapping2.used & 60
                session.commit()
    return redirect(url_for('getCoupon',user_name=user_name))

    



if __name__ == '__main__':
	application.debug = True
	application.run()
