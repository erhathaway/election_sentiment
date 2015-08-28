import os
import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Sequence, Float, Date, DateTime, BLOB, TEXT #, Date, Blob
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, UniqueConstraint

def _get_date():
  return datetime.datetime.now()

# get Base object
Base = declarative_base()

class Source(Base):
  __tablename__ = 'sources'
  id                    = Column(Integer, Sequence('source_id_seq', start=0, increment=1), primary_key=True)
  name                  = Column(String(250), unique=True, nullable=False)
  source_type           = Column(String(250), nullable=False)
  search_term_position  = Column(Integer)
  page_position         = Column(Integer)
  starting_page         = Column(String(250))
  search_url1           = Column(TEXT)
  search_url2           = Column(TEXT)
  search_url3           = Column(TEXT)
  created_at            = Column(DateTime, default=_get_date)
  updated_at            = Column(DateTime, onupdate=_get_date)

class Canidate(Base):
  __tablename__ = 'canidates'
  id          = Column(Integer, Sequence('canidate_id_seq', start=0, increment=1), primary_key=True)
  first_name  = Column(String(250), nullable=False)
  last_name   = Column(String(250), nullable=False)
  party       = Column(String(250), nullable=False)
  created_at  = Column(DateTime, default=_get_date)
  updated_at  = Column(DateTime, onupdate=_get_date)
  __table_args__ = (UniqueConstraint('first_name', 'last_name', name='full_name'),)

class Article(Base):
  __tablename__ = 'articles'
  id            = Column(Integer, Sequence('article_id_seq', start=0, increment=1), primary_key=True)
  source_id     = Column(Integer, ForeignKey('sources.id'), nullable=False)
  source        = relationship(Source)
  canidate_id   = Column(Integer, ForeignKey('canidates.id'), nullable=False)
  canidate      = relationship(Canidate)
  canidate_mention_count = Column(Integer)
  url           = Column(TEXT, unique=True, nullable=False)
  headline      = Column(TEXT, nullable=False)
  author_1      = Column(String(250), nullable=False)
  author_2      = Column(String(250), nullable=False)
  author_3      = Column(String(250), nullable=False)
  content       = Column(BLOB, unique=True)
  publish_date  = Column(Date, nullable=False)
  scrape_status = Column(String(250), nullable=False)
  created_at    = Column(DateTime, default=_get_date)
  updated_at    = Column(DateTime, onupdate=_get_date)
  __table_args__ = (UniqueConstraint('source_id', 'canidate_id', name='headline'),)

class Sentiment(Base):
  __tablename__ = 'sentiments'
  id          = Column(Integer, Sequence('sentiment_id_seq', start=0, increment=1), primary_key=True)
  score       = Column(Float, nullable=False)
  article_id  = Column(Integer, ForeignKey('articles.id'), nullable=False)
  article     = relationship(Article)
  created_at  = Column(DateTime, default=_get_date)
  updated_at  = Column(DateTime, onupdate=_get_date)

# Connect to db
engine = create_engine('sqlite:///database.db')
 
# Create all schema
Base.metadata.create_all(engine)
