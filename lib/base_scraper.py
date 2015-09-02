from bs4 import BeautifulSoup
from django.utils.encoding import smart_str, force_unicode
import re
import dryscrape
import os, sys
import datetime

#first change the cwd to the script path
scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
os.chdir(scriptPath)

#append the relative location you want to import from
sys.path.append("../db")

from declaratives import Article 

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

  def get_url(self, search_item):
    raise NotImplementedError

  def get_headline(self, search_item):
    raise NotImplementedError

  def get_author(self, search_item):
    raise NotImplementedError

  def get_date(self, search_item):
    raise NotImplementedError

  def get_summary(self, search_item): 
    raise NotImplementedError

  # @classmethod
  # def store_search(source_object, canidate_object):
  def store_search(self, source_id, canidate_id, verification_term, url, headline, author, date, summary):
    #init
    headline_raw = headline
    headline = headline.lower()

    if verification_term.lower() in headline:
      #see if already in database
      instance = self.session.query(Article).filter(Article.headline == headline).filter(Article.source_id == source_id).first()
      if instance:
        print "article already exists"
        return 1
      else:
        article = Article(
          source_id     = source_id,
          canidate_id   = canidate_id,
          url           = url,
          headline_raw  = headline_raw,
          headline      = headline,
          author_1      = author,
          pub_date  = date,
          scrape_status = "only scraped url")
        self.session.add(article)
        self.session.commit()
        return 0
    else:
      print "verification term not found in headline"
      # return 0 because status only looks at duplicates and
      # we don't want this to count towards the total duplicate count
      return 0

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
      if data != 1:
        return force_unicode(data)
      else:
        return 1
    except Exception, e:
      print e
      return 1

  # @staticmethod
  def get_search_results(self, source_object, canidate_object, max_duplicates=10, oldest_article_date = "01/01/2015"):
    #init
    duplicates = 0 
    page = 0
    date = datetime.datetime.today()
    oldest_article_date = datetime.datetime.strptime(oldest_article_date, '%m/%d/%Y') 
    
    #get info from db objects
    source_id = source_object.id
    canidate_id = canidate_object.id
    verification_term = canidate_object.last_name

    while duplicates < max_duplicates and date >= oldest_article_date :
      print date
      print oldest_article_date
      print " "
      page += 1
      #form search_term
      search_term = canidate_object.first_name + "+" + canidate_object.last_name
      # make url
      url = self.form_url(source_object, search_term, str(page))
      # make soup
      soup = self.make_soup(url)

      # parse html for date of interest    
      for search_item in self.iterable(soup):
        print duplicates
        print ""
        #extract data
        url       = self.validate(self.get_url(search_item))
        headline  = self.validate(self.get_headline(search_item))
        author    = self.validate(self.get_author(search_item))
        date      = self.validate(self.get_date(search_item))
        date      = datetime.datetime.strptime(date, '%B %d, %Y')
        summary   = self.validate(self.get_summary(search_item))

        #check to make sure data should be stored
        if duplicates >= max_duplicates:
          print "Max duplicates reached"
          return "Finish scraped"
        elif url != 1 and headline != 1 and author != 1 and date != 1 and summary !=1:
          # store data
          status = self.store_search(source_id, canidate_id, verification_term, url, headline, author, date, summary)
          # if data is NOT already in the database
          if status != 0:
            print status
            print "whhha"
            duplicates +=1
        else:
          print "Error storing search item"


      # for canidate in canidates:
        # search_template(canidate)

