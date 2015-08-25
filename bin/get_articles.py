# import mechanize
from bs4 import BeautifulSoup
# import urlparse
# import sys
# import os
import re

from django.utils.encoding import smart_str
import dryscrape


def find_articles_by_form(site, search_form_index, search_controler_name, search_term):
  browserSpecs = 'Mozilla/5.0 (X11; Linux x86_64; rv:18.0) Gecko/20100101 Firefox/18.0 (compatible;)'
  br = mechanize.Browser()
  br.set_handle_robots(False)
  br.addheaders = [('User-Agent', browserSpecs), ('Accept', '*/*')] # need ths to re-direct
  br.open(site)
  br.select_form(nr=search_form_index)
  br.form[search_controler_name]=search_term
  result = br.submit()
  print result.read()
  print result.geturl()

def find_articles_by_url(search_url1, slug, search_url2):
  # render html with dryscrape
  session = dryscrape.Session()
  session.visit(search_url1+slug+search_url2)
  eval_url = smart_str(session.url())
  html = session.body() 

  # create html soup
  soup = BeautifulSoup(html)
  search_results = soup.find("div", {"id": "searchResults"})
  
  # parse articles
  for x in search_results.find_all('li', {'class':"story"}):
    
    # url
    link = x.find('a', href=True)
    print "Found the URL:", link['href']
    
    # headline
    try:
      headline = x.find('span', {'class':"printHeadline"})
      print smart_str(headline.contents[0]) 
    except Exception as e:
      print e

    # author
    try:
      author =  x.find('span', {'class':"byline"})
      print smart_str(author.contents[0]) 
    except Exception as e:
      print e
    
    # date
    try:
      date = x.find('span', {'class':"dateline"})
      print smart_str(date.contents[0]) 
    except Exception as e:
      print e
    
    # summary 
    try:
      summary = x.find('p', {'class':"summary"})
      info = ""
      for i in summary.contents:
        if re.match('<.*>', smart_str(i)) is None:
          info += smart_str(i).strip() + " "
      print info
    except Exception as e:
      print e

    print " "

site = "http://www.nytimes.com"
search_url1 = "http://query.nytimes.com/search/sitesearch/?action=click&contentCollection&region=TopBar&WT.nav=searchWidget&module=SearchSubmit&pgtype=Homepage#/"
# search_url2 = "/since1851/allresults/1/allauthors/newest/"
search_url2 = ""
search_term = "rand paul"
# find_search(site)
# find_articles(site, 0, "search-input","texas is awesome")
find_articles_by_url(search_url1, search_term, search_url2)

