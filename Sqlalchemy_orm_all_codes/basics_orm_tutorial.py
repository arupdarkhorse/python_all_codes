from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker # for orm sqlalchemy

engine = create_engine('sqlite:///:memory:') #echo=True)
Base = declarative_base()

class User(Base):

    __tablename__ = "users"
    
    id = Column(Integer, Sequence('user_id_seq'),primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):

        return f"User(name={self.name}, fullname={self.fullname}, nickname={self.nickname})"
 
arup_user = User(id=1, name='arup', fullname='arup saint', nickname='Gopal')
jadu_user = User(id=2, name='Jadu', fullname='Jadu Saint', nickname='jamba')
komal_user = User(id=3, name='Komal', fullname='Komal Pandey', nickname='jhandu')
Base.metadata.create_all(engine)    # it issues a create table statement to database
#for orm sqlalchemy below sessionmaker, below is engine object available
#Session = sessionmaker(bind=engine)
# In the case where your application does not yet have an Engine when you define your module-level objects,
#  just set it up like below:
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
# adding user to session 
#session.add(arup_user)
#session.add(jadu_user)
session.add_all([arup_user, jadu_user, komal_user])
our_user = session.query(User).filter_by(name='arup').first()   # it acts like limit statement in mysql return the top value
'''
# looping across all the object to get data
all_user = session.query(User).all()    # same as all_user = session.query(User)
print(f"printing first user {our_user.name}")
for i in all_user:
    print(i.name)

session.commit()
print(session.dirty)
'''
primary_key_based_id = session.query(User).get(2)       # row based search on primary key
print(primary_key_based_id.name)
update_first_appln_orm = session.query(User).filter(User.id!=2).update({User.name : "Mr."+User.name}, synchronize_session=False)
print(update_first_appln_orm)
# for rolling back      session.rollback()
session.commit()
'''
for _ in session.query(User):
   print(_.name)

session.query(User).get(2).name = f"Mr.{session.query(User).get(2).name}"
session.commit()
session.rollback()
for _ in session.query(User):
   print(_.name)
'''
'''
print(session.query(User).filter(User.name.like('%Ja%')).name)
for _ in session.query(User).filter(User.name.like('%Ja%')):
    print(_.name)
'''
