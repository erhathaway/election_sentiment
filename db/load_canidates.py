import declaratives as de
from sqlalchemy.orm import sessionmaker
import csv

Session = sessionmaker(bind=de.engine)
session = Session()

file_name = 'canidates.csv'
csv_file = csv.DictReader(open(file_name, 'rb'), delimiter=',', quotechar='"')

for line in csv_file:
  canidate = de.Canidate(
    first_name  = line['first_name'],
    last_name   = line['last_name'],
    party       = line['party'])
  session.add(canidate)
  session.commit()