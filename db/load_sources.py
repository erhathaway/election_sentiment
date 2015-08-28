import declaratives
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
session = Session()

source = Source(name='Test',source_type="Test type")
session.add(source)
session.commit()