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

restaurant2 = Restaurant(name="Little Bangkok", category=1, 
	pic1='http://www.jadeinnchinesefood.com/1.jpg',
	pic2='http://www.kowloonnc.com/resources/img/backgrounds/chinese_2.jpg', 
	pic3='http://chinabuffetatlantic.com/custom/1.jpg', 
	coupon='coupon here!', 
	zipCode='30324')
session.add(restaurant2)
session.commit()

restaurant3 = Restaurant(name="Qing Mu", category=1, 
	pic1='http://www.thechinesequest.com/wp-content/uploads/2014/08/Chinese-food-facts.jpg',
	pic2='http://images.scrippsnetworks.com/up/tp/Scripps_-_Food_Category_Prod/423/982/0242666_4x3.jpg', 
	pic3='http://www.cheatsheet.com/wp-content/uploads/2015/04/eating-chinese-food-general-tsos-chicken1.jpg', 
	coupon='coupon here!', 
	zipCode='30305')
session.add(restaurant3)
session.commit()

restaurant4 = Restaurant(name="Ah-Mas Taiwanese Kitchen", category=1, 
	pic1='https://i.ytimg.com/vi/3T8JUuibXaI/maxresdefault.jpg',
	pic2='https://blogs-images.forbes.com/nickpassmore/files/2015/07/chinese.jpg', 
	pic3='http://www.no1chinesesouthorange.com/img/inside2.jpg', 
	coupon='coupon here!', 
	zipCode='30308')
session.add(restaurant4)
session.commit()

restaurant5 = Restaurant(name="Chow Bing", category=1, 
	pic1='http://greatwallchinesetopeka.com/wp-content/uploads/2012/01/bigstock_Chinese_Food_1640057-980x651.jpg',
	pic2='https://i.ytimg.com/vi/vbfvkyuGP9w/maxresdefault.jpg', 
	pic3='http://i2.cdn.cnn.com/cnnnext/dam/assets/150203151301-chinese-food-lanzhou-hand-pulled-noodles-exlarge-169.jpg', 
	coupon='coupon here!', 
	zipCode='30305')
session.add(restaurant5)
session.commit()

restaurant6 = Restaurant(name="Chinese Buddha", category=1, 
	pic1='https://image.shutterstock.com/z/stock-photo-sichuan-mapo-tofu-chinese-food-134522126.jpg',
	pic2='http://images.chinahighlights.com/allpicture/2015/11/02dfd30be09a4d2cb9fd6d4a_299x198.jpg', 
	pic3='http://del.h-cdn.co/assets/16/01/980x1470/gallery-1452121541-noodle-dishes-beef-broccoli.jpg', 
	coupon='coupon here!', 
	zipCode='30309')
session.add(restaurant6)
session.commit()

restaurant7 = Restaurant(name="Hong Kong Harbour", category=1, 
	pic1='http://del.h-cdn.co/assets/17/05/980x490/landscape-1485807729-delish-mongolian-beef-ramen-1.jpg',
	pic2='https://cimg1.ibsrv.net/cimg/www.fitday.com/693x350_100-1/1/17_UnhealthyChineseFood-108001.jpg', 
	pic3='http://www.creativechinese.com/wp-content/uploads/2014/08/297677-chinese-food-chinese-food.jpg', 
	coupon='coupon here!', 
	zipCode='30324')
session.add(restaurant7)
session.commit()

restaurant8 = Restaurant(name="Green Sprout", category=1, 
	pic1='http://rasamalaysia.com/images/thumbs/chow_mein.jpg',
	pic2='http://del.h-cdn.co/assets/16/07/buddhas-delight-11.jpg', 
	pic3='http://www.pacificohialeah.com/resources/img/backgrounds/chinese_6.jpg', 
	coupon='coupon here!', 
	zipCode='30324')
session.add(restaurant8)
session.commit()

restaurant9 = Restaurant(name="Chong Qing Hot Pot", category=1, 
	pic1='http://www.chinahighlights.com/image/food/central-food.jpg',
	pic2='http://blangua.com/uploads/blog/2016-03/the-mediterranean-food-festival-in-malta/logo_lg.png', 
	pic3='https://s3-media1.fl.yelpcdn.com/bphoto/EOqlWRakFCusWAegiq40dA/348s.jpg', 
	coupon='coupon here!', 
	zipCode='30341')
session.add(restaurant9)
session.commit()

restaurant10 = Restaurant(name="Suzy Sius Baos", category=1, 
	pic1='http://i.huffpost.com/gadgets/slideshows/328312/slide_328312_3188206_free.jpg',
	pic2='https://cbssacramento.files.wordpress.com/2016/02/chinesefood.jpg?w=625', 
	pic3='http://www.vodkitchen.com/wp-content/uploads/2012/04/D72_9466.jpg', 
	coupon='coupon here!', 
	zipCode='30307')
session.add(restaurant10)
session.commit()

# category 2: Indian Restaurant
restaurant1 = Restaurant(name="Amara", category=2, 
	pic1='http://az616578.vo.msecnd.net/files/2016/07/06/636034360643459128-507613226_indian.jpg',
	pic2='http://media.coreperformance.com/images/how-to-order-healthier-indian-food.jpg', 
	pic3='https://s-media-cache-ak0.pinimg.com/736x/40/76/9b/40769b23404b06d1414a4ff055cda673.jpg', 
	coupon='coupon here!', 
	zipCode='30307')
session.add(restaurant1)
session.commit()

restaurant2 = Restaurant(name="Copper Cove Indian Bistro", category=2, 
	pic1='http://static.wixstatic.com/media/f37000_13b7ca3387eb4f9dbef563fa9478744e.jpg_srz_1044_437_85_22_0.50_1.20_0.00_jpg_srz',
	pic2='https://static1.squarespace.com/static/56e95c49f850829a3e2bc17a/56ea66765559861e784c270c/56ea66778a65e25199c8a500/1458202234706/photodune-8502349-indian-food-saag-paneer-curry-dish-m.jpg?format=2500w', 
	pic3='http://www.bestofindiamn.com/custom/1.jpg', 
	coupon='coupon here!', 
	zipCode='30305')
session.add(restaurant2)
session.commit()

restaurant3 = Restaurant(name="ROTI: Vegetarian Indian Soul Food in EAV", category=2, 
	pic1='https://s3-media1.fl.yelpcdn.com/bphoto/EXTSO314rGAiW6gfst5shw/348s.jpg',
	pic2='http://www.indianfoodforever.com/images/desserts-indian.jpg', 
	pic3='http://img.sndimg.com/food/image/upload/v1/img/recipes/13/00/55/pic8m6qeF.jpg', 
	coupon='coupon here!', 
	zipCode='30316')
session.add(restaurant3)
session.commit()

restaurant4 = Restaurant(name="Tabla", category=2, 
	pic1='https://i.ytimg.com/vi/Xs0qex07RLQ/maxresdefault.jpg',
	pic2='https://i.ytimg.com/vi/S0PR0QLmwgI/maxresdefault.jpg', 
	pic3='https://s-media-cache-ak0.pinimg.com/originals/ca/8f/14/ca8f145daf893cd92e9302431077a32e.jpg', 
	coupon='coupon here!', 
	zipCode='30309')
session.add(restaurant4)
session.commit()

restaurant5 = Restaurant(name="Touch", category=2, 
	pic1='https://img.grouponcdn.com/deal/2QGXv1igQQ7fjqpqfixV/ei-700x420/v1/c700x420.jpg',
	pic2='https://s-media-cache-ak0.pinimg.com/736x/fe/72/5c/fe725ccf09c85c50586a9f600e077e5c.jpg', 
	pic3='https://s-media-cache-ak0.pinimg.com/564x/8d/ec/4f/8dec4f80df6486849600f833059c03fd.jpg', 
	coupon='coupon here!', 
	zipCode='30318')
session.add(restaurant5)
session.commit()

restaurant6 = Restaurant(name="Cafe Bombay", category=2, 
	pic1='http://www.indianfoodforever.com/images/indian-food-platter.jpg',
	pic2='http://aanganclassicindianandnepalese.com/custom/2.jpg', 
	pic3='http://www.haveliindianrestaurant.com/data1/images/banner3.jpg', 
	coupon='coupon here!', 
	zipCode='30329')
session.add(restaurant6)
session.commit()

restaurant7 = Restaurant(name="Botiwalla", category=2, 
	pic1='http://cdn.c.photoshelter.com/img-get/I0000d.azQDN.vB4/s/1000/Lamb-Keema-Indian-Food-Pictures-PWP11420.jpg',
	pic2='https://s-media-cache-ak0.pinimg.com/originals/d4/68/d8/d468d8dd2c911d8a16935b59f0e20154.jpg', 
	pic3='https://img.grouponcdn.com/deal/dNZD7X1GUcafsyiVpDVF/SM-4020x2412/v1/c700x420.jpg', 
	coupon='coupon here!',
	zipCode='30308')
session.add(restaurant7)
session.commit()

restaurant8 = Restaurant(name="Aamar Indian Cuisine", category=2, 
	pic1='https://s-media-cache-ak0.pinimg.com/originals/d2/f4/b7/d2f4b73c726ffd507cbb35f17841db54.jpg',
	pic2='http://www.indianfoodforever.com/images/indian-snacks.jpg', 
	pic3='http://3.bp.blogspot.com/-hMpL3mhguCk/VofI5kvDfVI/AAAAAAAABNE/BBoldZnblKg/s1600/angoori%2Brabdi.JPG', 
	coupon='coupon here!', 
	zipCode='30303')
session.add(restaurant8)
session.commit()

restaurant9 = Restaurant(name="Purnima Bangladeshi Cuisine", category=2, 
	pic1='http://dailygenius.com/wp-content/uploads/2016/03/2016-03-28T170200Z_1_MTZSPDEC3SRDZBRC_RTRFIPP_4_COOKING-INDIAN-FOOD-RECIPES.jpg',
	pic2='https://img.grouponcdn.com/deal/2QdjuCN19ha5weiyBibz/p1-3925x2355/v1/c700x420.jpg', 
	pic3='https://img.grouponcdn.com/deal/4XBo282maj26qNbGbZQA6FSUjMN9/4X-700x420/v1/c700x420.jpg', 
	coupon='coupon here!', 
	zipCode='30341')
session.add(restaurant9)
session.commit()

restaurant10 = Restaurant(name="Masti Indian Street Eats", category=2, 
	pic1='https://img.buzzfeed.com/buzzfeed-static/static/2015-11/3/5/enhanced/webdr08/enhanced-10906-1446548387-1.jpg',
	pic2='http://www.bollywoodtadkanj.com/assets/images/run_slider_07.jpg', 
	pic3='http://static.wixstatic.com/media/506ed2_2232c9f0184d518fbec11bfa8fa37930.jpg_srz_1280_850_85_22_0.50_1.20_0.00_jpg_srz', 
	coupon='coupon here!', 
	zipCode='30329')
session.add(restaurant10)
session.commit()

# Mexico Restaurant
restaurant1 = Restaurant(name="La Pastorcita", category=3, 
	pic1='http://www.foodofy.com/wp-content/uploads/2015/08/mexican-food-4.jpg',
	pic2='http://www.healthytravelblog.com/wp-content/uploads/2014/05/Mexican-Food.jpg', 
	pic3='https://s-media-cache-ak0.pinimg.com/originals/dd/2f/ea/dd2fea78093b9bad1d398f03319e2782.jpg', 
	coupon='coupon here!', 
	zipCode='30329')
session.add(restaurant1)
session.commit()

restaurant2 = Restaurant(name="La Parrilla Mexico Restaurant", category=3, 
	pic1='https://s-media-cache-ak0.pinimg.com/originals/83/5a/27/835a27263a83ddb5935f264a813e4969.jpg',
	pic2='https://s-media-cache-ak0.pinimg.com/originals/66/cd/b2/66cdb22bcb834603a692a44be40fe92d.png', 
	pic3='http://del.h-cdn.co/assets/16/02/980x653/gallery-1452896805-delish-lasagna-mexican-1.jpg', 
	coupon='coupon here!', 
	zipCode='30318')
session.add(restaurant2)
session.commit()

restaurant3 = Restaurant(name="Bone Garden Cantina", category=3, 
	pic1='https://1.bp.blogspot.com/-Fk_A_3GgUic/VtSUJ7mn2FI/AAAAAAAAJwc/j2RI6DI7Ahg/s1600/Tilapia%2BVeracruz%2BStyle%2B-3.jpg',
	pic2='https://www.roughguides.com/wp-content/uploads/2016/01/mexican-food-660x420.jpg', 
	pic3='http://www.eatlivetravelwrite.com/wp-content/uploads/2011/11/DSC_3492.jpg', 
	coupon='coupon here!', 
	zipCode='30318')
session.add(restaurant3)
session.commit()

restaurant4 = Restaurant(name="The Original EI Taco", category=3, 
	pic1='http://fromshorestoskylines.smugmug.com/Mexico/Mexico-Food/i-jNx27Bw/0/L/P8170151-L.jpg',
	pic2='http://i1.wp.com/www.foodrepublic.com/wp-content/uploads/2016/06/Big-Juan-burger-1.jpg?resize=700%2C%20519', 
	pic3='https://www.lib.utexas.edu/d7/sites/default/files/branch/benson/images/events/santibanez%20street%20food.jpg', 
	coupon='coupon here!', 
	zipCode='30306')
session.add(restaurant4)
session.commit()

restaurant5 = Restaurant(name="Uncle Julio's Fine Mexican Food", category=3, 
	pic1='http://www.foodofy.com/wp-content/uploads/2015/08/mexican-food-8.jpg',
	pic2='http://www.destination360.com/north-america/mexico/images/s/mexico-food.jpg', 
	pic3='https://s-media-cache-ak0.pinimg.com/originals/43/2c/3c/432c3c0b5ab6753ab96cd9ceb7b08349.jpg', 
	coupon='coupon here!', 
	zipCode='30309')
session.add(restaurant5)
session.commit()

restaurant6 = Restaurant(name="Rosa Mexican", category=3, 
	pic1='http://www.escapeartist.com/mexico/wp-content/uploads/sites/14/2011/09/Mexican-Food-1.jpg',
	pic2='http://www.foodrepublic.com/wp-content/uploads/2013/03/uFIST_3pYtv7_K7T_1Qh0UXDKqGO7YzNEwhAdTtImfM-1024x630.jpg', 
	pic3='http://images.media-allrecipes.com/images/55484.jpg', 
	coupon='coupon here!', 
	zipCode='30363')
session.add(restaurant6)
session.commit()

restaurant7 = Restaurant(name="Rreal Tacos", category=3, 
	pic1='http://www.billyparisi.com/wp-content/uploads/mexican-food-010.jpg',
	pic2='https://lavca.org/wp-content/uploads/2017/01/InnovaCamp-Ventures-Food-Start-ups-Mexico.jpg', 
	pic3='http://cdn-jpg.thedailymeal.net/sites/default/files/story/CROP%20MEX.jpg', 
	coupon='coupon here!', 
	zipCode='30308')
session.add(restaurant7)
session.commit()

restaurant8 = Restaurant(name="Escorpion", category=3, 
	pic1='http://www.foodofy.com/wp-content/uploads/2015/08/mexican-food-2.jpg',
	pic2='http://tapasmagazine.com/wp-content/uploads/2015/03/MEXICO-600x480.jpg', 
	pic3='http://static6.businessinsider.com/image/553e56096da811d609c5c918/21-mouthwatering-photos-of-authentic-mexican-food.jpg', 
	coupon='coupon here!', 
	zipCode='30308')
session.add(restaurant8)
session.commit()

restaurant9 = Restaurant(name="Nuevo Laredo Cantina", category=3, 
	pic1='http://s.eatthis-cdn.com/media/images/ext/228532206/queso.jpg',
	pic2='http://static.ifood.tv/files/image/d0/23/543829-authentic-mexican-cuisine.jpg', 
	pic3='http://papasmexicangrill.com/wp-content/uploads/2012/07/Fajita1140-400-b-1080x379.jpg', 
	coupon='coupon here!', 
	zipCode='30318')
session.add(restaurant9)
session.commit()

restaurant10 = Restaurant(name="Tacos & Tequilas Mexican Grill", category=3, 
	pic1='https://d36tnp772eyphs.cloudfront.net/blogs/1/2014/11/Calabacitas_MJ_1200x.jpg',
	pic2='https://www.bloomberg.com/features/2016-best-restaurants-mexico-city/img/2016-best-restaurants-mexico-city-facebook.png', 
	pic3='https://img.grouponcdn.com/deal/ffBTYpGD6AYc888jWShQ/YA-2048x1229/v1/c700x420.jpg', 
	coupon='coupon here!', 
	zipCode='30308')
session.add(restaurant10)
session.commit()

# category 4 French Restaurant
restaurant1 = Restaurant(name="Anis Bistro", category=4, 
	pic1='http://www.kids-world-travel-guide.com/images/french_food_macarons_shutterstock_62967172-2.jpg',
	pic2='http://easyscienceforkids.com/wp-content/uploads/2014/02/All-about-Crepes-and-Other-French-Foods-Fun-Facts-for-Kids-image-of-French-Banana-Crepes.jpeg', 
	pic3='https://s-media-cache-ak0.pinimg.com/originals/cc/56/14/cc56142db7d74ed2c9d20f9c85abbe73.jpg', 
	coupon='coupon here!', 
	zipCode='30305')
session.add(restaurant1)
session.commit()

restaurant2 = Restaurant(name="Babette's Cafe", category=4, 
	pic1='http://www.expatica.com/media/upload/714582.jpg',
	pic2='https://happywanderer15.files.wordpress.com/2012/09/img_1713.jpg', 
	pic3='http://www.expatica.com/media/upload/714581.jpg', 
	coupon='coupon here!', 
	zipCode='30307')
session.add(restaurant2)
session.commit()

restaurant3 = Restaurant(name="Atmosphere", category=4, 
	pic1='http://i.ndtvimg.com/i/2016-03/french-cheese-625_625x350_51458292019.jpg',
	pic2='http://cf.ltkcdn.net/french/images/std/185902-425x283-cream-puffs.jpg', 
	pic3='http://www.recipe4living.com/assets/itemimages/400/400/3/7b2d8de5af7e817620b6a620db9574e5_147022403.jpg', 
	coupon='coupon here!', 
	zipCode='30324')
session.add(restaurant3)
session.commit()

restaurant4 = Restaurant(name="Bistro Niko", category=4, 
	pic1='http://cf.ltkcdn.net/french/images/slide/124687-849x565-cheese.jpg',
	pic2='https://www.easy-french-food.com/image-files/chocolate_eclair.jpg', 
	pic3='https://www.frenchentree.com/wp-content/uploads/2015/08/shutterstock_167996741.jpg', 
	coupon='coupon here!', 
	zipCode='30326')
session.add(restaurant4)
session.commit()

restaurant5 = Restaurant(name="Le Biboquet", category=4, 
	pic1='https://s-media-cache-ak0.pinimg.com/originals/5f/0a/96/5f0a968f7d365f006e695ece4a58463d.jpg',
	pic2='http://del.h-cdn.co/assets/cm/15/11/54fdf2db52d89-bacon-leek-quiche-xl.jpg', 
	pic3='http://www.fluentu.com/french/blog/wp-content/uploads/sites/3/2014/06/essential-French-food-vocabulary-regional-cuisines-pancakes.jpg', 
	coupon='coupon here!', 
	zipCode='30305')
session.add(restaurant5)
session.commit()

restaurant6 = Restaurant(name="Marcel", category=4, 
	pic1='http://www.saveur.com/sites/saveur.com/files/styles/large_1x_/public/images/2015/03/vegetables_barigoule-of-spring-vegetables_2000x1500.jpg?itok=hrVzbHA2',
	pic2='https://s-media-cache-ak0.pinimg.com/originals/d9/6f/5d/d96f5ddd0b572724755c7405883fe4b9.jpg', 
	pic3='https://s-media-cache-ak0.pinimg.com/736x/3c/ed/e4/3cede4873291ed4825bd0c46eb9d9e3b.jpg', 
	coupon='coupon here!', 
	zipCode='30318')
session.add(restaurant6)
session.commit()

restaurant7 = Restaurant(name="Cafe Alsace", category=4, 
	pic1='http://www.saveur.com/sites/saveur.com/files/styles/large_4x3/public/images/2015/03/recipe_homard-en-croute-lobster-pot-pie_500x750.jpg?itok=-Bt5nah0&fc=50,50',
	pic2='http://www.fluentu.com/french/blog/wp-content/uploads/sites/3/2014/06/essential-French-food-vocabulary-regional-cuisines-duck-confit.jpg', 
	pic3='https://onceuponaspice.files.wordpress.com/2015/05/icd24lk.jpg', 
	coupon='coupon here!', 
	zipCode='30030')
session.add(restaurant7)
session.commit()

restaurant8 = Restaurant(name="Petite Auberge", category=4, 
	pic1='http://ii.worldmarket.com/fcgi-bin/iipsrv.fcgi?FIF=/images/worldmarket/source/63108_XXX_v1.tif&wid=358%20&cvt=jpeg',
	pic2='https://www.alux.com/wp-content/uploads/2013/08/url.jpeg', 
	pic3='http://i.ndtvimg.com/i/2017-01/french-cheese-bread-620_620x350_81483514231.jpg', 
	coupon='coupon here!', 
	zipCode='30329')
session.add(restaurant8)
session.commit()

restaurant9 = Restaurant(name="Cafe Vendome", category=4, 
	pic1='http://www.charlestoncvb.com/cvb-plan-visit/assets/images/timthumb/timthumb.php?w=400&h=300&src=http://www.charlestoncvb.com/assets/images/listings/original_http://www.charlestoncvb.com/assets/images/listings/original_-2-Custom-.jpg&1',
	pic2='https://www.discoverwalks.com/blog/wp-content/uploads/2016/07/french-food-big.jpg', 
	pic3='http://www.fluentu.com/french/blog/wp-content/uploads/sites/3/2014/06/essential-French-food-vocabulary-regional-cuisines2.jpg', 
	coupon='coupon here!', 
	zipCode='30324')
session.add(restaurant9)
session.commit()

restaurant10 = Restaurant(name="Another Broken Egg Cafe", category=4, 
	pic1='http://www.france-voyage.com/visuals/pratique/enjoying-french-cuisine-29-1_w1000.jpg',
	pic2='https://s-media-cache-ak0.pinimg.com/originals/40/01/3c/40013c09b40e45657e984974bcc0a9e9.jpg', 
	pic3='http://i.ndtvimg.com/i/2016-11/foei-gras_650x400_71479412260.jpg', 
	coupon='coupon here!', 
	zipCode='30321')
session.add(restaurant10)
session.commit()

# category 5: Cafe Restaurant
restaurant1 = Restaurant(name="Ebrik Coffee Room", category=5, 
	pic1='http://cdn.cdkitchen.com/images/cats/88/cat-88-720-1.jpg',
	pic2='https://www.craveamerica.com/wp-content/uploads/2015/10/dessert.jpg', 
	pic3='http://www.kraftrecipes.com/-/media/assets/2016-festive/black-forest-mousse-dessert-90590-642x428.jpg?h=428&w=642&la=en&hash=E62BAAECA731AA536DA5813C7ACFCD64DD3A6AE3', 
	coupon='coupon here!', 
	zipCode='30303')
session.add(restaurant1)
session.commit()

restaurant2 = Restaurant(name="Octane", category=5, 
	pic1='http://www.kraftrecipes.com/-/media/assets/festive15_heroes/philadelphia-mini-cheesecakes-143464-642x428.jpg?h=428&w=642&la=en&hash=3D00A3A011D578159C5174B8ACDD60548A5BECAD',
	pic2='https://images6.alphacoders.com/434/434430.jpg', 
	pic3='http://www.drodd.com/images15/dessert24.jpg', 
	coupon='coupon here!', 
	zipCode='30318')
session.add(restaurant2)
session.commit()

restaurant3 = Restaurant(name="Revolution Doughnut", category=5, 
	pic1='http://www.cheatsheet.com/wp-content/uploads/2014/11/Chocolate-Pudding-640x425.jpg',
	pic2='http://rasamalaysia.com/wp-content/uploads/2015/06/Berry-Cheesecake-Bars-thumb.jpg', 
	pic3='https://images3.alphacoders.com/190/190135.jpg', 
	coupon='coupon here!', 
	zipCode='30307')
session.add(restaurant3)
session.commit()

restaurant4 = Restaurant(name="Land of a Thousand Hills Coffee", category=5, 
	pic1='https://eat24-files-live.s3.amazonaws.com/cuisines/v4/dessert.jpg?Signature=dUAtr3BLC11%2BcezsFsrYNJUyBT4%3D&Expires=1490000047&AWSAccessKeyId=AKIAIEJ2GCCJRT63TBYA',
	pic2='http://cdn.skim.gs/images/Strawberry-cake_rkcasu/memorial-day-dessert-recipes', 
	pic3='http://www.drodd.com/images15/dessert28.jpg', 
	coupon='coupon here!', 
	zipCode='30363')
session.add(restaurant4)
session.commit()

restaurant5 = Restaurant(name="Octane Coffee / Bar - Arts Center", category=5, 
	pic1='http://clv.h-cdn.co/assets/15/10/980x490/landscape_1425677897-54eaed1ad41f2_-_wn-sugar-balsamic-strawberry-sauce-recipe-clx0514-igyovu-s2.jpg',
	pic2='https://www.howtocookthat.net/public_html/wp-content/uploads/2015/08/IMG_9167-550x413.jpg?4118d5', 
	pic3='http://images6.fanpop.com/image/photos/36800000/Dessert-food-36849259-2560-1600.jpg', 
	coupon='coupon here!', 
	zipCode='30309')
session.add(restaurant5)
session.commit()

restaurant6 = Restaurant(name="Dancing Goat Coffee Bar", category=5, 
	pic1='http://eskipaper.com/images/dessert-1.jpg',
	pic2='http://lovethiscitytv.com/wp-content/uploads/2015/06/Best-Dessert-Places-in-Toronto2.jpg', 
	pic3='http://assets.marthastewart.com/styles/wmax-1500/d29/med104768_0709_raspberry_mess/med104768_0709_raspberry_mess_sq.jpg?itok=jCRYp7HO', 
	coupon='coupon here!', 
	zipCode='30308')
session.add(restaurant6)
session.commit()

restaurant7 = Restaurant(name="Cafe Vendome", category=5, 
	pic1='http://www.kraftcanada.com/-/media/kraft%20canada/recipes/620x423/c/chocolate-caramel-brownies-152180.jpg?h=423&w=620',
	pic2='http://sweetservings.com/wp-content/uploads/2014/02/cocoa-lounge-dessert-bar-at-island-hotel.jpg', 
	pic3='http://cdn-image.foodandwine.com/sites/default/files/201112-xl-brandy-mascarpone-semifreddo.jpg', 
	coupon='coupon here!', 
	zipCode='30342')
session.add(restaurant7)
session.commit()

restaurant8 = Restaurant(name="Java Saga", category=5, 
	pic1='http://images.media-allrecipes.com/images/67695.jpg',
	pic2='https://media1.popsugar-assets.com/files/thumbor/GvOBmszRlVfVSXyd5EkKLTmRW7c/fit-in/1024x1024/filters:format_auto-!!-:strip_icc-!!-/2016/06/23/913/n/1922195/0c6fb33e_edit_img_cover_file_41754189_1466712325_123/i/Restaurant-Dessert-Copycat-Recipes.jpg', 
	pic3='https://www.mcdonalds.com/us/en-us/full-menu/desserts-and-shakes/_jcr_content/par/category/mobile.img.jpg/1484066425454.jpg', 
	coupon='coupon here!', 
	zipCode='30309')
session.add(restaurant8)
session.commit()

restaurant9 = Restaurant(name="Cafe Lucia", category=5, 
	pic1='http://del.h-cdn.co/assets/15/32/tiramisu-mousse-5-of-8.jpg',
	pic2='http://assets.marthastewart.com/styles/wmax-520-highdpi/d35/apple-cider-doughnut-cake-102877650/apple-cider-doughnut-cake-102877650_sq.jpg?itok=CYXqfOJq', 
	pic3='http://img.huffingtonpost.com/asset/,scalefit_600_noupscale/561e63001400002b003c8337.jpeg', 
	coupon='coupon here!', 
	zipCode='30303')
session.add(restaurant9)
session.commit()

restaurant10 = Restaurant(name="Sweet Hut Backery & Cafe", category=5, 
	pic1='http://cdn2.tmbi.com/TOH/Images/Photos/37/1200x1200/exps33498_5SD153598B11_05_2b.jpg',
	pic2='http://www.ndtv.com/cooks/images/mince.pies.jpg', 
	pic3='http://www.jameshotels.com/polopoly_fs/1.2221.1377615111!/fileImage/httpImage/image.jpg_gen/derivatives/landscape_1615/jny-restaurant-davidburke-menus-dessert-chocolatecake-06182013-jpg.jpg', 
	coupon='coupon here!', 
	zipCode='30309')
session.add(restaurant10)
session.commit()

# category 6: Spanish Restaurant
restaurant1 = Restaurant(name="Alma Cocina", category=6, 
	pic1='http://www.expatica.com/media/upload/776693.jpg',
	pic2='http://caminoways.com/media/Spanish-Food.jpg', 
	pic3='http://www.simpleyrecipes.com/lib/038/894-food1-do-bite-into-some-spanish-food-for-the-best-of-taste-and-variety.jpg', 
	coupon='coupon here!', 
	zipCode='30303')
session.add(restaurant1)
session.commit()

restaurant2 = Restaurant(name="Gypsy Kitchen", category=6, 
	pic1='https://www.colourbox.com/preview/7313019-spanish-cuisine-assorted-tapas-on-ceramic-plates.jpg',
	pic2='http://www.thetapaslunchcompany.co.uk/IMG_1267.jpg', 
	pic3='http://www.bbc.co.uk/schools/primarylanguages_assets/spanish/images/foodanddrink_tapas.jpg', 
	coupon='coupon here!', 
	zipCode='30305')
session.add(restaurant2)
session.commit()

restaurant3 = Restaurant(name="Buen Provecho", category=6, 
	pic1='https://www.bascofinefoods.com/media/wysiwyg/spanish-food-online-uk-specialists_3.jpg',
	pic2='http://omglifestyle.com/wp-content/uploads/2014/03/Paella.jpg', 
	pic3='http://www.expatica.com/media/upload/776696.jpg',
	coupon='coupon here!', 
	zipCode='30367')
session.add(restaurant3)
session.commit()

restaurant4 = Restaurant(name="Saltyard", category=6, 
	pic1='http://www.expatica.com/media/upload/776699.jpg',
	pic2='http://bonitonorte.com/wp-content/uploads/2016/03/tortilla_patatas-672xXx80.jpg', 
	pic3='https://ymuchomas.files.wordpress.com/2013/12/spain-christmas-prawns.jpg', 
	coupon='coupon here!', 
	zipCode='30309')
session.add(restaurant4)
session.commit()

restaurant5 = Restaurant(name="Cooks & Sodiers", category=6, 
	pic1='http://foodsecret.com/wp-content/uploads/2015/10/Spanish-Food.jpg',
	pic2='https://9227-presscdn-0-11-pagely.netdna-ssl.com/wp-content/uploads/2012/10/IMG_5249.jpg', 
	pic3='https://previews.123rf.com/images/iloveotto/iloveotto1103/iloveotto110300405/9182092-closeup-of-prawn-with-rice-traditionnal-spanish-food-paella-Stock-Photo.jpg', 
	coupon='coupon here!', 
	zipCode='30318')
session.add(restaurant5)
session.commit()

restaurant6 = Restaurant(name="Tapa Tapa", category=6, 
	pic1='https://s-media-cache-ak0.pinimg.com/originals/f9/cb/dc/f9cbdc652458a5140e2cf41a62081ea6.jpg',
	pic2='http://i2.cdn.cnn.com/cnnnext/dam/assets/160929100653-essential-spanish-dish-fabada-super-169.jpg', 
	pic3='http://newmedia.thomson.co.uk/live/vol/0/672bd9f9edccfa2b5fce0dd78cb9d6d51182e35f/1080x608/web/EUROPEMEDITERRANEANTURKEYCON_TURTURKEY-BODRUMTORBAGONCABALIKTORBAMARINA.jpg', 
	coupon='coupon here!', 
	zipCode='30308')
session.add(restaurant6)
session.commit()

restaurant7 = Restaurant(name="Papi's Cuban & Caribbean Grill", category=6, 
	pic1='https://media.halaltrip.com/other/wp-content/uploads/2015/10/halal-food-in-spain-paella.jpg',
	pic2='http://www.thetapaslunchcompany.co.uk/Depositphotos_4377751_M.jpg', 
	pic3='http://www.spanish-food.org/images/tocinillo-slide.jpg', 
	coupon='coupon here!', 
	zipCode='30308')
session.add(restaurant7)
session.commit()

restaurant8 = Restaurant(name="Barcelona Westside Ironworks", category=6, 
	pic1='https://d25rq8gxcq0p71.cloudfront.net/language-guide/758/paella.jpg',
	pic2='http://www.open.edu/openlearn/ocw/pluginfile.php/775611/mod_resource/content/0/l194_2_cover_image_1%20(1).jpg', 
	pic3='http://blog.topdeck.travel/wp-content/uploads/2016/10/spain-food-pulpo-octopus.jpg', 
	coupon='coupon here!', 
	zipCode='30318')
session.add(restaurant8)
session.commit()

restaurant9 = Restaurant(name="Barcelona Inman Park", category=6, 
	pic1='http://farm8.staticflickr.com/7160/6448938035_05a4dd2a88.jpg',
	pic2='http://food.fnr.sndimg.com/content/dam/images/food/fullset/2010/10/29/1/CCWID110_Smoky-Spanish-Hunters-Chicken_s4x3.jpg.rend.hgtvcom.1280.960.jpeg', 
	pic3='https://pbs.twimg.com/media/C2YCD8vXUAATsE_.jpg', 
	coupon='coupon here!', 
	zipCode='30307')
session.add(restaurant9)
session.commit()

restaurant10 = Restaurant(name="Eclipse Di Luna", category=6, 
	pic1='https://s-media-cache-ak0.pinimg.com/originals/f4/fb/df/f4fbdf210c28a5ee6b603557b673e8c6.jpg',
	pic2='http://www.delicioso.co.uk/themes/Delicioso/images/header3.jpg', 
	pic3='http://learnenglishteens.britishcouncil.org/sites/teens/files/styles/article/public/istock_000011589470small.jpg?itok=jvBpw9Z_', 
	coupon='coupon here!', 
	zipCode='30324')
session.add(restaurant10)
session.commit()

# category 7: American Restaurant
restaurant1 = Restaurant(name="Georgia Grill", category=7, 
	pic1='http://ghk.h-cdn.co/assets/cm/15/11/54ffec52236b6-cheeseburger-lgn.jpg',
	pic2='https://www.waiter.com/blog/wp-content/uploads/2015/06/hamburger.jpg', 
	pic3='http://www.fluentu.com/english/blog/wp-content/uploads/sites/4/2014/05/fourth-july-picnic-english-vocabulary-american-food2.jpg', 
	coupon='coupon here!', 
	zipCode='30309')
session.add(restaurant1)
session.commit()

restaurant2 = Restaurant(name="Amara", category=7, 
	pic1='https://s-media-cache-ak0.pinimg.com/736x/5e/22/59/5e2259bcc187ec96bd2e5ee2613762c5.jpg',
	pic2='http://provoscene.com/wp-content/uploads/2014/04/american-food-middle-estonia-46ea04be2173ce0e52d5123a59564527.jpg', 
	pic3='http://cdni.condenast.co.uk/646x430/a_c/corn-dogs-easy-living-4jul13-istock_b_646x430.jpg', 
	coupon='coupon here!', 
	zipCode='30307')
session.add(restaurant2)
session.commit()

restaurant3 = Restaurant(name="Double Zero", category=7, 
	pic1='http://i.ndtvimg.com/i/2015-07/pancake-625_625x350_41435922828.jpg',
	pic2='https://img.grouponcdn.com/deal/k3EyCBD149fq3nSARny/ft-2048x1229/v1/c700x420.jpg', 
	pic3='https://thoughtcatalog.files.wordpress.com/2014/04/shutterstock_115964296.jpg?w=584&h=390', 
	coupon='coupon here!', 
	zipCode='30307')
session.add(restaurant3)
session.commit()

restaurant4 = Restaurant(name="Fortune Cookies", category=7, 
	pic1='http://nebula.wsimg.com/b489204e07cc8f09efd5988c845cb148?AccessKeyId=667A17726E9A9A5A56A9&disposition=0&alloworigin=1',
	pic2='https://img.grouponcdn.com/deal/buVZUK4y1zPNtknudpBg/t8-2048x1229/v1/c700x420.jpg', 
	pic3='https://img.buzzfeed.com/buzzfeed-static/static/2016-08/23/21/campaign_images/buzzfeed-prod-fastlane03/22-times-france-was-better-at-american-food-than--2-6155-1472002634-0_dblbig.jpg', 
	coupon='coupon here!', 
	zipCode='30326')
session.add(restaurant4)
session.commit()

restaurant5 = Restaurant(name="Rock's Kitchen & Fries", category=7, 
	pic1='https://img.grouponcdn.com/deal/35WA1xakMb8jJnRYfJJb/Xt-2048x1229/v1/c700x420.jpg',
	pic2='http://mividaen.sampere.com/wp-content/uploads/2014/09/American-food.jpg', 
	pic3='https://img.grouponcdn.com/deal/3zUkZTYwW7dNjGjEF7e3uGw4HqE6/3z-700x420/v1/c700x420.jpg', 
	coupon='coupon here!', 
	zipCode='30326')
session.add(restaurant5)
session.commit()

restaurant6 = Restaurant(name="Georgia's Restaurant & Bar", category=7, 
	pic1='http://i.ndtvimg.com/i/2015-07/smores-625_625x350_81435923035.jpg',
	pic2='https://i.ytimg.com/vi/QxqZqiXu9fE/hqdefault.jpg', 
	pic3='https://img.grouponcdn.com/deal/qJQc35gT6KKsVVFcmNDjxb/super_7_pizza_shoppe-2048x1229/v1/c700x420.jpg', 
	coupon='coupon here!', 
	zipCode='zipCode here!')
session.add(restaurant6)
session.commit()

restaurant7 = Restaurant(name="Cook Hall", category=7, 
	pic1='https://img.grouponcdn.com/deal/cVNg9ApctUAH7wJpPPk9/yD-700x420/v1/c700x420.jpg',
	pic2='http://www.listchallenges.com/f/lists/1f9f67c7-bf0e-4782-8840-02b9858cf0f8.jpg', 
	pic3='https://img.grouponcdn.com/deal/Ar8A9NaQhCgzSmYZca5/TW-4200x2520/v1/c700x420.jpg', 
	coupon='coupon here!', 
	zipCode='30326')
session.add(restaurant7)
session.commit()

restaurant8 = Restaurant(name="American Cut", category=7, 
	pic1='http://i.huffpost.com/gadgets/slideshows/349045/slide_349045_3725414_free.jpg',
	pic2='https://fthmb.tqn.com/SRMiAAFSVW_h49tCkuSB5UZgqzk=/1500x1126/filters:fill(transparent,1)/about/PunchIndex-88563482-56a171d55f9b58b7d0bf5884.jpg', 
	pic3='https://fthmb.tqn.com/KP7hALXHuF1qpHlQ7PfSZDR4bfU=/350x0/about/Stocksy_txpb81932ee3rN100_Medium_741391-58b05d9d5f9b5860468fe29b.jpg', 
	coupon='coupon here!', 
	zipCode='30305')
session.add(restaurant8)
session.commit()

restaurant9 = Restaurant(name="Holeman & Finch", category=7, 
	pic1='http://www.americanfoodsupplygroup.com/wp-content/uploads/2015/06/lobster-752705_1280-e1437678750128.jpg',
	pic2='https://i.ytimg.com/vi/ATB-o2JSQ10/maxresdefault.jpg', 
	pic3='https://www.theurbanlist.com/images/made/content/article/best-american-food-melbourne_740_486_s_c1.jpg', 
	coupon='coupon here!', 
	zipCode='30309')
session.add(restaurant9)
session.commit()

restaurant10 = Restaurant(name="The Hungry Peach", category=7, 
	pic1='https://media1.popsugar-assets.com/files/2010/07/27/1/192/1922195/43506804397e276e_quiz_american_dish_origins.preview.jpg',
	pic2='https://img.grouponcdn.com/iam/bDvedvp886CQBLCLHA2q/x3-2592x1555/v1/c700x420.jpg', 
	pic3='https://img.grouponcdn.com/deal/c6Xanyp8PYHmZ8kQHPLd/y4-700x420/v1/c700x420.jpg', 
	coupon='coupon here!', 
	zipCode='30305')
session.add(restaurant10)
session.commit()

# category 8: Italian Restaurant
restaurant1 = Restaurant(name="Princi Italia", category=8, 
	pic1='http://pictures.food.com/api/file/jM62DXCrT1aecxGU1bEc-Authentic-Italian-Meatballs---92095-4.JPG/convert?loc=/pictures.food.com/recipes/92/09/5/biEOgaNLQUCDi2mvSmX8_Authentic%20Italian%20Meatballs%20-%2392095-4.JPG',
	pic2='http://img.sndimg.com/food/image/upload/q_92,fl_progressive/v1/img/recipes/18/46/93/i7Z2TV5NRUCIboq7BbdD_veg-lasagna-roll-ups-3.jpg', 
	pic3='http://viztangocafe.com/wp-content/uploads/2015/06/food2.jpg', 
	coupon='coupon here!', 
	zipCode='30309')
session.add(restaurant1)
session.commit()

restaurant2 = Restaurant(name="Double Zero", category=8, 
	pic1='https://alianosdundee.com/file/2015/12/Italian-Pasta-in-East-Dundee-IL-Alianos-Italian-Food.jpg',
	pic2='https://www.deliverywow.com/order-food-online/images/main-photo-chicago-italian-food-delivery.jpg', 
	pic3='http://mahapunjab.com/wp-content/uploads/2016/10/Italian-Food-Chandigarh.jpg', 
	coupon='coupon here!', 
	zipCode='30307')
session.add(restaurant2)
session.commit()

restaurant3 = Restaurant(name="Ecco", category=8, 
	pic1='http://i.ndtvimg.com/i/2015-12/italian_625x350_41450863014.jpg',
	pic2='http://media.dish.allrecipes.com/wp-content/uploads/2015/09/2429762_Microwave-Mexican-Manicotti_139726_Photo-by-bd.weld_.jpg', 
	pic3='http://i.ndtvimg.com/i/2016-03/caprese-salad-625_625x350_81459344578.jpg', 
	coupon='coupon here!', 
	zipCode='30308')
session.add(restaurant3)
session.commit()

restaurant4 = Restaurant(name="Dolce Italian", category=8, 
	pic1='https://eat24-files-live.s3.amazonaws.com/cuisines/v4/italian.jpg?Signature=fu2oqUciXdLaP4XOFWzh7alc4PQ%3D&Expires=1490066848&AWSAccessKeyId=AKIAIEJ2GCCJRT63TBYA',
	pic2='https://media-cdn.tripadvisor.com/media/photo-s/05/80/e9/95/bob-s-italian-food-imports.jpg', 
	pic3='http://www.carolinasitalianrestaurant.com/slide/h4.jpg', 
	coupon='coupon here!', 
	zipCode='30305')
session.add(restaurant4)
session.commit()

restaurant5 = Restaurant(name="Ninos Italian Restaurant", category=8, 
	pic1='https://www.healthydiningfinder.com/getattachment/03acf00d-a184-44c4-a23b-6669fe86c49c/20-Ways-to-Cut-Calories-at-Italian-Restaurants.aspx',
	pic2='http://i.huffpost.com/gen/935109/images/o-ITALIAN-FOOD-RECIPES-PASTA-facebook.jpg', 
	pic3='http://www.cs.trinity.edu/~sholguin/images/pizza.jpg', 
	coupon='coupon here!', 
	zipCode='30324')
session.add(restaurant5)
session.commit()

restaurant6 = Restaurant(name="La Grotta Ristrorante Italian", category=8, 
	pic1='https://img.grouponcdn.com/deal/vtaF3tgw41rKcE9Kc3KZhj/146767840-2048x1229/v1/c700x420.jpg',
	pic2='http://foodnetwork.sndimg.com/content/dam/images/food/fullset/2015/8/7/1/FN_Italian-Favorites-Opener_s4x3.jpg', 
	pic3='https://s-media-cache-ak0.pinimg.com/originals/09/5c/bb/095cbb14dd12bfba671ce7bbdabac5a3.jpg', 
	coupon='coupon here!', 
	zipCode='30305')
session.add(restaurant6)
session.commit()

restaurant7 = Restaurant(name="Valenza", category=8, 
	pic1='http://pestos.net/images/pestos-food-home.jpg',
	pic2='http://peterborough.storetown.net/upload/cmspage/mattoni%5Eabout-us/31-01-14_11-37-15_italian-food-el-cajon.jpg', 
	pic3='http://hz5m11s95uy3wtavm1hkpiw1.wpengine.netdna-cdn.com/files/2007/07/foodpage4.jpg', 
	coupon='coupon here!', 
	zipCode='30307')
session.add(restaurant7)
session.commit()

restaurant8 = Restaurant(name="BoccaLupo", category=8, 
	pic1='http://finditranchocucamonga.com/wp-content/uploads/2015/11/Italian-Food1.jpg',
	pic2='https://media.timeout.com/images/100750515/image.jpg', 
	pic3='http://avolios.com/italian-restaurant/wp-content/uploads/2014/08/sl3.png', 
	coupon='coupon here!', 
	zipCode='30307')
session.add(restaurant8)
session.commit()

restaurant9 = Restaurant(name="La Tavola Trattroia", category=8, 
	pic1='http://www.getawayantalya.com/wp-content/uploads/2014/09/image-it.jpg',
	pic2='https://www.chiapparellis.com/img/CR-Lunch.png', 
	pic3='http://riviste.newbusinessmedia.it/wp-content/uploads/sites/27/2013/10/IS1DAI1071.jpg', 
	coupon='coupon here!', 
	zipCode='30306')
session.add(restaurant9)
session.commit()

restaurant10 = Restaurant(name="Pasta Da Pulcinella", category=8, 
	pic1='https://static.mgmresorts.com/content/dam/MGM/excalibur/dining/buca-di-beppo/excalibur-restaurants-buca-di-beppo-spaghetti-wine-.tif.image.1152.550.high.jpg',
	pic2='http://del.h-cdn.co/assets/15/35/1600x800/landscape-1440698647-italian-kebab-delish.jpg', 
	pic3='https://images.blogthings.com/theitalianfoodtest/italian-food-3.jpg', 
	coupon='coupon here!', 
	zipCode='30309')
session.add(restaurant10)
session.commit()

# category 9: Japanese Restaurant
restaurant1 = Restaurant(name="Wagaya Japenese Restaurant", category=9, 
	pic1='http://i2.cdn.cnn.com/cnnnext/dam/assets/160823141245-japan-food6-hiroshima-ramen-hiroshima-prefecturejnto-exlarge-169.jpg',
	pic2='https://www.bbcgoodfood.com/sites/default/files/styles/recipe/public/recipe_images/recipe-image-legacy-id--1222479_11.jpg?itok=YnLBanOy', 
	pic3='http://www.timetravelturtle.com/wp-content/uploads/2013/04/Japan-2013-414_web-sbar.jpg', 
	coupon='coupon here!', 
	zipCode='30318')
session.add(restaurant1)
session.commit()

restaurant2 = Restaurant(name="Ginya Izakaya", category=9, 
	pic1='https://fthmb.tqn.com/qA8W1A46wmMetr5aZN0T95hWKZY=/3604x2766/filters:no_upscale()/about/GettyImages-184989995-56b38fd03df78cf7385cbcbb.jpg',
	pic2='http://themewallpapers.com/wp-content/uploads/2014/02/Sushi-Food.jpg', 
	pic3='http://i2.cdn.cnn.com/cnnnext/dam/assets/160823141827-japan-food17-yamaguchi-yakitori-jnto-super-169.jpg', 
	coupon='coupon here!', 
	zipCode='30318')
session.add(restaurant2)
session.commit()

restaurant3 = Restaurant(name="Nakato Japanese Restaurant", category=9, 
	pic1='https://previews.123rf.com/images/lsantilli/lsantilli1207/lsantilli120700134/14333834-fresh-sushi-traditional-japanese-food-Stock-Photo.jpg',
	pic2='https://s-media-cache-ak0.pinimg.com/originals/f4/52/44/f452443b6464cb2884d8dfb844bfc93b.jpg', 
	pic3='http://muza-chan.net/aj/poze-weblog4/dango.jpg', 
	coupon='coupon here!', 
	zipCode='30324')
session.add(restaurant3)
session.commit()

restaurant4 = Restaurant(name=" Umi", category=9, 
	pic1='http://www.japan-guide.com/g9/106_01b.jpg',
	pic2='http://3u1bxj4dc91n2voz2e27rlg0.wpengine.netdna-cdn.com/six-two/wp-content/uploads/2015/08/japanese-food-2-1024x576.jpg', 
	pic3='http://www.timetravelturtle.com/wp-content/uploads/2013/04/Japan-2013-26_web-sbar.jpg', 
	coupon='coupon here!', 
	zipCode='30305')
session.add(restaurant4)
session.commit()

restaurant5 = Restaurant(name="Miso Izakaya", category=9, 
	pic1='https://previews.123rf.com/images/gloriaolsy/gloriaolsy1111/gloriaolsy111100405/11359492-Traditional-Japanese-food-Sushi-Closeup-japanese-sushi-on-a-bamboo-napkin-Sushi-collection-Stock-Photo.jpg',
	pic2='http://cdna.tid.al/46669fc68a839b3d87d51548951a3b80e464d23e.png', 
	pic3='https://s-media-cache-ak0.pinimg.com/originals/c1/53/a5/c153a5fe7abdcfe6b1387c1ece044338.jpg', 
	coupon='coupon here!', 
	zipCode='30312')
session.add(restaurant5)
session.commit()

restaurant6 = Restaurant(name="Upper Room", category=9, 
	pic1='https://img.grouponcdn.com/iam/nH6B1h6NiXUEPc5fBG5s/gQ-2048x1229/v1/c700x420.jpg',
	pic2='https://www.healthable.org/wp-content/uploads/2015/02/Japanese-Food.jpg', 
	pic3='http://muza-chan.net/aj/poze-weblog4/japanese-food-zaru-soba-big.jpg', 
	coupon='coupon here!', 
	zipCode='30326')
session.add(restaurant6)
session.commit()

restaurant7 = Restaurant(name="Hajime", category=9, 
	pic1='https://himg-6298.kxcdn.com/wp-content/uploads/2015/02/Japanese-Food1.jpg',
	pic2='https://eat24-files-live.s3.amazonaws.com/cuisines/v4/japanese.jpg?Signature=E5ixhB%2F4klsIpgf%2BZyn6CTM4eqg%3D&Expires=1490077011&AWSAccessKeyId=AKIAIEJ2GCCJRT63TBYA', 
	pic3='http://i2.cdn.cnn.com/cnnnext/dam/assets/160823141447-japan-food22-hamamatsu-eel-hvbcjnto-super-169.jpg', 
	coupon='coupon here!', 
	zipCode='30324')
session.add(restaurant7)
session.commit()

restaurant8 = Restaurant(name="Nexto", category=9, 
	pic1='http://az616578.vo.msecnd.net/files/2016/09/16/636096556837713079-2107039032_sushi-japanese-food-rice-japah.jpg',
	pic2='http://www.vietnamvisa-easy.com/blog/wp-content/uploads/2013/10/japanese-food-festival-vietnam-visa-on-arrival.jpg', 
	pic3='http://jpninfo.com/wp-content/uploads/2016/08/japanese-food-cat-bento.png', 
	coupon='coupon here!', 
	zipCode='30306')
session.add(restaurant8)
session.commit()

restaurant9 = Restaurant(name="O-Ku Sushi", category=9, 
	pic1='http://foodjunction.fastglobalbiz.com/wp-content/uploads/2015/10/Suci.jpg',
	pic2='http://cdn.tokyotimes.com/wp-content/uploads/2013/03/japanese-food.jpg', 
	pic3='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Tempura,_sashimi,_pickles,_ris_og_misosuppe_(6289116752).jpg/1200px-Tempura,_sashimi,_pickles,_ris_og_misosuppe_(6289116752).jpg', 
	coupon='coupon here!', 
	zipCode='30318')
session.add(restaurant9)
session.commit()

restaurant10 = Restaurant(name="Tomo Japanese Restaurant", category=9, 
	pic1='http://cdn.skim.gs/images/v1/msi/fvc7d7csgmaak7703rfn/things-only-people-who-love-japanese-food-will-understand',
	pic2='http://www.oyatsubox.com/wp-content/uploads/Food.jpg', 
	pic3='https://financesonline.com/uploads/2014/06/food4.jpg', 
	coupon='coupon here!', 
	zipCode='30326')
session.add(restaurant10)
session.commit()

# category 10: korean restaurant
restaurant1 = Restaurant(name="Char Korean Bar & Grill", category=10, 
	pic1='http://esquireuk.cdnds.net/15/37/980x490/980x490-londons-best-korean-food-final-43-jpg-3f200a3b.jpg',
	pic2='https://fthmb.tqn.com/oSfuvKEe3MmV8c11w4pBvsigOl8=/350x250/filters:no_upscale()/about/151577823-56a57a083df78cf772888a64.jpg', 
	pic3='https://upload.wikimedia.org/wikipedia/commons/5/51/Korean.food-Kimbap-03.jpg', 
	coupon='coupon here!', 
	zipCode='30307')
session.add(restaurant1)
session.commit()

restaurant2 = Restaurant(name="So Kong Dong Tofu House", category=10, 
	pic1='http://www.foodrepublic.com/wp-content/uploads/2015/11/korean-restaurant-philadelphia-cover-page.jpg',
	pic2='http://www.elizabethwoyke.com/wp-content/uploads/2014/12/Korean-food-500.jpg', 
	pic3='http://ww3.hdnux.com/photos/36/15/36/7919502/17/920x920.jpg', 
	coupon='coupon here!', 
	zipCode='30340')
session.add(restaurant2)
session.commit()

restaurant3 = Restaurant(name="Blossom Tree", category=10, 
	pic1='http://www.sweetsharing.com/wp-content/uploads/2015/06/southkorean-food2.jpg',
	pic2='http://www.seriouseats.com/images/2014/08/korean-food-momofuku-ssam-bar-spicy-rice-cakes-robyn-lee.jpg', 
	pic3='https://media.timeout.com/images/102523828/image.jpg', 
	coupon='coupon here!', 
	zipCode='30303')
session.add(restaurant3)
session.commit()

restaurant4 = Restaurant(name="Kwans Deli and Korean Kitchen", category=10, 
	pic1='https://eat24-files-live.s3.amazonaws.com/cuisines/v4/korean.jpg?Signature=B41p7qjWfkw00r4oaocplE44%2BS0%3D&Expires=1490077839&AWSAccessKeyId=AKIAIEJ2GCCJRT63TBYA',
	pic2='http://www.fnstatic.co.uk/images/content/recipe/korean-bbq-kalbi.jpeg', 
	pic3='http://www.eatandtravelwithus.com/wp-content/uploads/2014/08/K-Cook-Korean-BBQ-Buffet-Seafood.jpg', 
	coupon='coupon here!', 
	zipCode='30313')
session.add(restaurant4)
session.commit()

restaurant5 = Restaurant(name="Gaja Korean Bar", category=10, 
	pic1='https://static1.squarespace.com/static/537ea499e4b098977ffcc96f/t/5388d342e4b0574568600602/1401475920660/wine+pairing+korean+food',
	pic2='https://media1.popsugar-assets.com/files/thumbor/B_1fNm9TlyeL5q_uginnZAcS5bo/fit-in/550x550/filters:format_auto-!!-:strip_icc-!!-/2012/03/11/4/192/1922195/af3f8afee375dee7_korean_food_primer_main.jpg', 
	pic3='http://zone-thebestsingapore.bhxtb9xxzrrdpzhqr.netdna-cdn.com/wp-content/uploads/2014/06/Big-Mama-Korean-Food.jpg', 
	coupon='coupon here!', 
	zipCode='30316')
session.add(restaurant5)
session.commit()

restaurant6 = Restaurant(name="Stone Bowl House -Woo Nam Jeong", category=10, 
	pic1='https://lh6.googleusercontent.com/-JknCkRrtg0o/ToluWWKT-jI/AAAAAAAAAKQ/_znsmydt_Ss/korea-food.jpg',
	pic2='https://migrationology.com/wp-content/uploads/2012/05/kim-chi.jpg', 
	pic3='https://www.maangchi.com/wp-content/uploads/2015/02/koreanfood.jpg', 
	coupon='coupon here!', 
	zipCode='30309')
session.add(restaurant6)
session.commit()

restaurant7 = Restaurant(name="Heirloom Market BBQ", category=10, 
	pic1='https://img.buzzfeed.com/buzzfeed-static/static/2015-01/27/16/campaign_images/webdr04/a-beginners-guide-to-eating-at-a-korean-restaurant-2-12894-1422395599-22_dblbig.jpg',
	pic2='https://wxlwxlnicole.files.wordpress.com/2015/04/weheartit.jpg', 
	pic3='http://cdn.koreaboo.com/wp-content/uploads/2014/11/new_BBQ-Tasting-Set.jpg', 
	coupon='coupon here!', 
	zipCode='30318')
session.add(restaurant7)
session.commit()

restaurant8 = Restaurant(name="Kang Nam", category=10, 
	pic1='http://monipag.com/clemence-anquetin/wp-content/uploads/sites/1656/2016/01/korean-food.png',
	pic2='https://img.buzzfeed.com/buzzfeed-static/static/2016-11/11/13/campaign_images/buzzfeed-prod-fastlane01/26-delicious-korean-foods-you-need-in-your-life-2-25004-1478890499-0_dblbig.jpg', 
	pic3='https://i.ytimg.com/vi/RUxugNYxFqg/maxresdefault.jpg', 
	coupon='coupon here!', 
	zipCode='30340')
session.add(restaurant8)
session.commit()

restaurant9 = Restaurant(name="Hankook Taqueria", category=10, 
	pic1='http://www.seriouseats.com/images/2015/08/20150802-annandale-korean-food-brian-oh-Jangwon.jpg',
	pic2='https://img.grouponcdn.com/deal/miW2aX61Q86hoqcMsLAL/j1-700x420/v1/c700x420.jpg', 
	pic3='http://sura-ri.com/public/images/slider/KOREAN-BANCHAN.jpg', 
	coupon='coupon here!', 
	zipCode='30318')
session.add(restaurant9)
session.commit()

restaurant10 = Restaurant(name="Simply Seoul", category=10, 
	pic1='https://charlotteagenda-charlotteagenda.netdna-ssl.com/wp-content/uploads/2015/05/korean-food.jpg',
	pic2='https://missconfig.files.wordpress.com/2015/05/samgyupsal.jpg', 
	pic3='https://media.licdn.com/mpr/mpr/shrinknp_800_800/AAEAAQAAAAAAAAOKAAAAJDRhMjNiZGNhLTExOTEtNDM2My1hOGY3LTlkZjU2MmYzM2YwZQ.jpg', 
	coupon='coupon here!', 
	zipCode='30308')
session.add(restaurant10)
session.commit()
# add users

user2=User(name='Bob', preference=1023, zipCode='zipCode',image='http://www.clipartbest.com/cliparts/aTe/6pk/aTe6pkAqc.jpg')
session.add(user2)
session.commit()

user3=User(name='Candy', preference=0, zipCode='zipCode',image='http://your-insurer.com/wp-content/uploads/2015/01/Agent-Sing2.jpg')
session.add(user3)
session.commit()

user4=User(name='David', preference=0, zipCode='zipCode',image='https://userscontent2.emaze.com/images/ef511f5d-96fa-4e7e-a7e1-49db36a8e9a2/715509f9d4ef6b01e018135121a72623.jpg')
session.add(user4)
session.commit()

user5=User(name='Eric',preference=0, zipCode='zipCode',image='http://www.tonydczech.com/Tony_Cartoon.jpg')
session.add(user5)
session.commit()

user6=User(name='Frank', preference=0, zipCode='zipCode',image='https://s-media-cache-ak0.pinimg.com/236x/df/4a/bd/df4abd207e53c233928a67e0ce2c71ee.jpg')
session.add(user6)
session.commit()

user7=User(name='George', preference=0, zipCode='zipCode',image='https://s-media-cache-ak0.pinimg.com/originals/2b/91/e7/2b91e763053b29f2b4995f901de34417.jpg')
session.add(user7)
session.commit()

user8=User(name='Hebe', preference=0, zipCode='zipCode',image='http://kastorskorner.com/wp/wp-content/uploads/2015/06/BUBBLES_01_PR-265x300.jpg')
session.add(user8)
session.commit()

user9=User(name='Iris', preference=0, zipCode='zipCode',image='https://s-media-cache-ak0.pinimg.com/736x/4b/53/55/4b53554766a2ed8fe948c08b09f37b1b.jpg')
session.add(user9)
session.commit()

user10=User(name='Jason', preference=0, zipCode='zipCode',image='http://comedycentral.mtvnimages.com/images/show_images/TVE_Hub_ShowImage_DrawnTogether.jpg?')
session.add(user10)
session.commit()

user1=User(name='Mary', preference=0, zipCode='zipCode',image='http://www.counsellingathome.com/wp-content/uploads/2015/07/Adrian-Holmes-Cartoon-Profile.jpg')
session.add(user1)
session.commit()
# add Mappings
# TODO: ADD MAPPINGS

# map1=Mapping(source='Mary',target='Eric',coupon1='La Tavola Trattroia',couple2='Char Korean Bar & Grill',couple3='Holeman & Finch',pending=1)
# session.add(map1)
# session.commit()

# map2=Mapping(source='Mary',target='Iris',coupon1='Gaja Korean Bar',couple2='La Tavola Trattroia',couple3='BoccaLupo',pending=1)
# session.add(map2)
# session.commit()

# map3=Mapping(source='George',target='Mary',coupon1='Upper Room',couple2='Heirloom Market BBQ',couple3='Ecco',pending=1)
# session.add(map3)
# session.commit()


# map4=Mapping(source='Jason',target='Mary',coupon1='Upper Room',couple2='Heirloom Market BBQ',couple3='Ecco',pending=1)
# session.add(map4)
# session.commit()













