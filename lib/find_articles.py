import os, sys

#first change the cwd to the script path
scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
os.chdir(scriptPath)

#append the relative location you want to import from
sys.path.append("../db")
sys.path.append("../bin")

import declaratives as de
from NYTimes import NYTimes

# from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=de.engine)
session = Session()

# instantiate object with orm db session
nytimes = NYTimes(session)

canidates = session.query(de.Canidate)
sources = session.query(de.Source)

print sources[0].name

for canidate in canidates:
  print "----------------------------------"
  print canidate.last_name
  print "----------------------------------"

  nytimes.get_search_results(sources[0],canidate)



# our_user = session.query(User).filter_by(name='ed').first() 
# print our_user
# ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
# session.add(ed_user)

# print ed_user.name