# sqlalchemy tollkit imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# Database classes imports
from catalog_database import Base, Categories, CatalogItem, User
import datetime
engine = create_engine('postgresql://catalog:catalog@localhost/catalog')
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


# Create users
User1 = User(name="Hana Shamatah",
             email="hanashamata@gmail.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')  # noqa
session.add(User1)
session.commit()

User2 = User(name="hana shamatah",
             email="hanashamata31@gmail.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')  # noqa
session.add(User2)
session.commit()

# Add Categories
category1 = Categories(user_id=User1.id, name="Formal")  # user_id=1
session.add(category1)
session.commit()

category2 = Categories(user_id=User1.id, name="Casual")  # user_id=1
session.add(category2)
session.commit()

category3 = Categories(user_id=User1.id, name="Sport")  # user_id=1
session.add(category3)
session.commit()

# category4 = Categories(user_id=User1.id, name="Homewear")
# session.add(category4)
# session.commit()

# category5 = Categories(user_id=User1.id, name="Underwear")
# session.add(category5)
# session.commit()

# category6 = Categories(user_id=User1.id, name="Accessories")
# session.add(category6)
# session.commit()


# Add catalog items
# For category1
catalogItem1 = CatalogItem(user_id=User1.id,
                           category_name=category1.name,
                           name="Jacket",
                           description="Make your formal wear a stylish one wearing a formal jacket. Perfect for your night events. Pair it with an off white shirt and black trousers with black leather shoes to make your outfit look picture perfect. ",  # noqa
                           picture="https://the-collective.imgix.net/img/app/product/1/199864-600150.jpg?w=610&auto=format",  # noqa
                           date=datetime.datetime.now())
session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=User1.id,
                           category_name=category1.name,
                           name="Suit",
                           description="For your wedding and it is perfect for very formal events",  # noqa
                           picture="https://i.pinimg.com/236x/ae/d0/65/aed0651106b6bc4b62b93f76020191f8.jpg",
                           date=datetime.datetime.now())
session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=User1.id,
                           category_name=category1.name,
                           name="Dressy Jacket",
                           description="Create your formal look for business or evening wear with Dressy Jackets",  # noqa
                           picture="http://www.gifttolive.com/wp-content/uploads/2018/01/jackets-womens-calvin-klein-dressy-denim-seamed-topper-jacket-indigo.jpg",  # noqa
                           date=datetime.datetime.now())
session.add(catalogItem3)
session.commit()

catalogItem4 = CatalogItem(user_id=User1.id,
                           category_name=category1.name,
                           name="Tie",
                           description="Black bow tie (silk, satin, or twill)",  # noqa
                           picture="https://i.pinimg.com/236x/05/e5/e5/05e5e544e49fe5b0d397653c6a9584cb.jpg",
                           date=datetime.datetime.now())
session.add(catalogItem4)
session.commit()

catalogItem5 = CatalogItem(user_id=User1.id,
                           category_name=category1.name,
                           name="Dress Coat",
                           description="A woman's dress that resembles an overcoat, usually with collar, lapels and front fastenings similar to a coat",  # noqa
                           picture="https://www.suzannah.com/images/product/zoom/couture-princess-coat-navy-blue-twill.jpg",  # noqa
                           date=datetime.datetime.now())
session.add(catalogItem5)
session.commit()

catalogItem6 = CatalogItem(user_id=User1.id,
                           category_name=category1.name,
                           name="Shirt",
                           description="White pique wing-collared shirt with stiff front",  # noqa
                           picture="https://static5.cilory.com/235372-large_default/french-connection-white-formal-shirt.jpg",  # noqa
                           date=datetime.datetime.now())
session.add(catalogItem6)
session.commit()

catalogItem7 = CatalogItem(user_id=User1.id,
                           category_name=category1.name,
                           name="Cufflinks",
                           description="Cufflinks are items of jewelry that are used to secure the cuffs of dress shirts. ",  # noqa
                           picture="https://i.pinimg.com/564x/ff/3e/85/ff3e85a2a77d66cda7c405405b6fdd33.jpg",
                           date=datetime.datetime.now())
session.add(catalogItem7)
session.commit()

catalogItem8 = CatalogItem(user_id=User1.id,
                           category_name=category1.name,
                           name="Gloves",
                           description="Ladies' evening gloves or opera gloves are a type of formal glove that reaches beyond the elbow. ",  # noqa
                           picture="https://i.pinimg.com/564x/c3/76/9e/c3769edf36501879c20b68f061737b20.jpg",
                           date=datetime.datetime.now())
session.add(catalogItem8)
session.commit()

catalogItem9 = CatalogItem(user_id=User1.id,
                           category_name=category1.name,
                           name="Shoes",
                           description="Step out in style in a pair of handcrafted leather shoes.",  # noqa
                           picture="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgsdNYm36qeuf2AOCkT8GETykunitDOwyIALGKzOA00a3KGKi-QQ",  # noqa
                           date=datetime.datetime.now())
session.add(catalogItem9)
session.commit()


# For category2
catalogItem10 = CatalogItem(user_id=User1.id,
                            category_name=category2.name,
                            name="Tshirt",
                            description="Look great and stay comfortable with short sleeves and a round neckline",  # noqa
                            picture="https://i.pinimg.com/564x/c3/76/9e/c3769edf36501879c20b68f061737b20.jpg",
                            date=datetime.datetime.now())
session.add(catalogItem10)
session.commit()

catalogItem11 = CatalogItem(user_id=User1.id,
                            category_name=category2.name,
                            name="Jeans",
                            description="A casual pants for daily use",  # noqa
                            picture="https://i.pinimg.com/236x/ad/a1/ae/ada1aec034004ad3c5f6392b71f73240.jpg",
                            date=datetime.datetime.now())
session.add(catalogItem11)
session.commit()

catalogItem12 = CatalogItem(user_id=User1.id,
                            category_name=category2.name,
                            name="Shorts",
                            description="Worn in warm weather or in an environment where comfort and air flow are more important than the protection of the legs",  # noqa
                            picture="https://i.pinimg.com/236x/3c/6a/df/3c6adfb7832bde8506a9526d487b7650.jpg",
                            date=datetime.datetime.now())
session.add(catalogItem12)
session.commit()

catalogItem13 = CatalogItem(user_id=User1.id,
                            category_name=category2.name,
                            name="Turtleneck",
                            description="A high collar that covers most of your neck even when the collar is folded over itself",  # noqa
                            picture="https://i.pinimg.com/564x/1f/70/bd/1f70bdab7726ee2162f3a808fb770ae2.jpg",
                            date=datetime.datetime.now())
session.add(catalogItem13)
session.commit()

catalogItem13 = CatalogItem(user_id=User1.id,
                            category_name=category2.name,
                            name="Blouse",
                            description="a loose-fitting garment resembling a shirt for women. A long-sleeved, collared button-down shirt is an example of a blouse.",  # noqa
                            picture="https://i.pinimg.com/564x/e3/e3/e5/e3e3e5e425fc8e26392431dc5e2e5335.jpg",
                            date=datetime.datetime.now())
session.add(catalogItem13)
session.commit()

catalogItem14 = CatalogItem(user_id=User1.id,
                            category_name=category2.name,
                            name="Skirt",
                            description="a free-hanging part of an outer garment or undergarment extending from the waist down",  # noqa
                            picture="https://i.pinimg.com/564x/fe/d2/5c/fed25c9af92ad8f2e2cc2ed2c2169bb5.jpg",
                            date=datetime.datetime.now())
session.add(catalogItem14)
session.commit()

# For category3
catalogItem15 = CatalogItem(user_id=User1.id,
                            category_name=category3.name,
                            name="Jersey",
                            description="a shirt worn as part of a uniform in sports such as football",  # noqa
                            picture="https://i.pinimg.com/236x/d8/f3/c4/d8f3c4b5beeb0f4067c56846e4517f63.jpg",
                            date=datetime.datetime.now())
session.add(catalogItem15)
session.commit()

catalogItem16 = CatalogItem(user_id=User1.id,
                            category_name=category3.name,
                            name="Shorts or Leggings",
                            description="comfortable shorts are a must for a successful trip to the gym",  # noqa
                            picture="https://i.pinimg.com/236x/69/6e/0e/696e0e75b7fef0cc8912f2f5efda3611.jpg",
                            date=datetime.datetime.now())
session.add(catalogItem16)
session.commit()

catalogItem17 = CatalogItem(user_id=User1.id,
                            category_name=category3.name,
                            name="Fitness Tank or Tee",
                            description="A lightweight tank top offers plenty of ventilation and flexibility",  # noqa
                            picture="https://i.pinimg.com/564x/e6/87/83/e687833df523a70067d525472ea9f5f2.jpg",
                            date=datetime.datetime.now())
session.add(catalogItem17)
session.commit()

catalogItem18 = CatalogItem(user_id=User1.id,
                            category_name=category3.name,
                            name="Sports Bra",
                            description="For women a good sports bra is everything, you will feel pretty miserable by the end of your workout",  # noqa
                            picture="https://i.pinimg.com/236x/9a/bb/19/9abb1989223955158e0a12e8a53d73d8.jpg",
                            date=datetime.datetime.now())
session.add(catalogItem18)
session.commit()

catalogItem19 = CatalogItem(user_id=User1.id,
                            category_name=category3.name,
                            name="Socks",
                            description="The socks lightweight running socks or low-cut socks with moisture-wicking, breathable fabric and a touch of arch support are a pretty big part of your gym comfort equation.",  # noqa
                            picture="https://i.pinimg.com/564x/bd/46/f9/bd46f9f9fc17e4be7f47374d4c510557.jpg",
                            date=datetime.datetime.now())
session.add(catalogItem19)
session.commit()

catalogItem20 = CatalogItem(user_id=User1.id,
                            category_name=category3.name,
                            name="Training Shoes",
                            description="The most essential item in sports",  # noqa
                            picture="https://i.pinimg.com/564x/0c/10/cc/0c10cc1023b75a29efebe132da59c8bf.jpg",
                            date=datetime.datetime.now())
session.add(catalogItem20)
session.commit()
print "added menu items!"
