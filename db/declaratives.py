from sqlalchemy import create_engine
engine = create_engine('sqlite:///database.db', echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String, Sequence
class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, Sequence('user_id_seq', start=0, increment=1), primary_key=True)
  name = Column(String)
  fullname = Column(String)
  password = Column(String)
  def __repr__(self):
    return "<User(name='%s', fullname='%s', password='%s')>" % (
                          self.name, self.fullname, self.password)



Base.metadata.create_all(engine) 
