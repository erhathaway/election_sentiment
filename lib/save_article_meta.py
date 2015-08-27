from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///../db/database.db')

Session = sessionmaker(bind=engine)

session = Session()

our_user = session.query(User).filter_by(name='ed').first() 
print our_user
# ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
# session.add(ed_user)

# print ed_user.name