import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Sequence, Float #, Date, Blob
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()

class Source(Base):
  __tablename__ = 'sources'
  id  = Column(Integer, Sequence('source_id_seq', start=0, increment=1), primary_key=True)
  name = Column(String(250), unique=True, nullable=False)
  source_type = Column(String(250), nullable=False)

class Canidate(Base):
  __tablename__ = 'canidates'
  id = Column(Integer, Sequence('canidate_id_seq', start=0, increment=1), primary_key=True)
  first_name = Column(String(250), nullable=False)
  last_name = Column(String(250), nullable=False)
  party = Column(String(250), nullable=False)

class Article(Base):
  __tablename__ = 'articles'
  id = Column(Integer, Sequence('article_id_seq', start=0, increment=1), primary_key=True)
  source_id = Column(Integer, ForeignKey('sources.id'), nullable=False)
  source = relationship(Source)
  canidate_id = Column(Integer, ForeignKey('canidates.id'), nullable=False)
  canidate = relationship(Canidate)
  canidate_metion_count = Column(Integer)
  url = Column(String(2000), unique=True, nullable=False)
  headline = Column(String(2000), nullable=False)
  author_1 = Column(String(2000), nullable=False)
  author_2 = Column(String(2000), nullable=False)
  author_3 = Column(String(2000), nullable=False)
  # contents = Column(BLOB, unique=True)
  # publish_date = Column(Date, nullable=False)
  scrape_status = Column(String(250), nullable=False)

class Sentiment(Base):
  __tablename__ = 'sentiments'
  id = Column(Integer, Sequence('sentiment_id_seq', start=0, increment=1), primary_key=True)
  score = Column(Float, nullable=False)
  article_id = Column(Integer, ForeignKey('articles.id'), nullable=False)
  article = relationship(Article)

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///database.db')
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)