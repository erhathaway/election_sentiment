import os, sys

#first change the cwd to the script path
scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
os.chdir(scriptPath)

#append the relative location you want to import from
sys.path.append("../db")

import declaratives as de
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=de.engine)
session = Session()


# itterate through all canidates in db
canidates = session.query(de.Canidate)

for person in canidates :
  print (person.first_name + " " + person.last_name).lower()
  print person.id

  # itterate through all sources in db
sources = session.query(de.Source)

for source in sources:
  print source.name 
  print source.id
  