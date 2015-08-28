import declaratives as de
from sqlalchemy.orm import sessionmaker
import csv

Session = sessionmaker(bind=de.engine)
session = Session()

file_name = 'sources.csv'
csv_file = csv.DictReader(open(file_name, 'rb'), delimiter=',', quotechar='"')

for line in csv_file:
  source = de.Source(
    name                  = line['name'],
    source_type           = line['source_type'],
    search_term_position  = line['search_term_position'],
    page_position         = line['page_position'],
    starting_page         = line['starting_page'],
    search_url1           = line['search_url1'],
    search_url2           = line['search_url2'],
    search_url3           = line['search_url3'])
  session.add(source)
  session.commit()

