from bs4 import BeautifulSoup
from django.utils.encoding import smart_str
import re
import dryscrape

class BaseScraper():
  """Extendable scraper object used to scrape websites"""

  def __init__(self, session):
    self.session = session

  def make_soup(self, url):
    # render html with dryscrape
    session = dryscrape.Session()
    session.visit(url)
    eval_url = smart_str(session.url())
    html = session.body() 

    # create html soup
    soup = BeautifulSoup(html)
    return soup

  def iterable(self, soup):
    raise NotImplementedError

  def url(self, search_item):
    raise NotImplementedError

  def headline(self, search_item):
    raise NotImplementedError

  def author(self, search_item):
    raise NotImplementedError

  def date(self, search_item):
    raise NotImplementedError

  def summary(self, search_item): 
    raise NotImplementedError

  @classmethod
  def store_search(source_object, canidate_object):
    pass

  @classmethod
  def store_content():
    pass

  # @staticmethod
  def form_url(self, source_object, search_term, page):
    s = source_object
    if s.search_term_position == 0 and s.page_position == 1:
      return s.search_url1 + search_term + s.search_url2 + page + s.search_url3 
    elif s.search_term_position == 1 and s.page_position == 2:
      return s.search_url1 + page + s.search_url2 + search_term + s.search_url3

  # @staticmethod
  def validate(self, data):
    try:
      print data
      return data
    except Exception, e:
      print e
      return 0

  # @staticmethod
  def get_search_results(self, source_object, canidate_object, max_duplicates=10):
    #test
    print source_object.name

    #init
    duplicates = 0 
    page = '1'
    
    #get ids
    source_id = source_object.id
    canidate_id = canidate_object.id

    #form search_term
    search_term = canidate_object.first_name + "+" + canidate_object.last_name
    print search_term
    # make url
    url = self.form_url(source_object, search_term, page)
    print url
    # make soup
    soup = self.make_soup(url)

    # parse html for date of interest    
    for search_item in self.iterable(soup):
      # print search_item
      #extract data
      url       = self.validate(url(search_item))
      headline  = self.validate(headline(search_item))
      author    = self.validate(author(search_item))
      date      = self.validate(date(search_item))
      summary   = self.validate(summary(search_item))
      # print url
      # print headline
      #check to make sure data should be stored
      if duplicates >= max_duplicates:
        print "Max duplicates reached"
        return "Finish scraped"
      elif url != 0 and headline != 0 and author != 0 and date != 0 and summary !=0:
        # store data
        status = store_search(source_id, canidate_id, url, headline, author, date, summary)
        # if data is NOT already in the database
        if status != 0:
          duplicates +=1
      else:
        print "Error storing search item"


    # for canidate in canidates:
      # search_template(canidate)

