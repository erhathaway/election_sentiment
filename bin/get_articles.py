import mechanize
from bs4 import BeautifulSoup
import urlparse
import sys
import os
import re

from django.utils.encoding import smart_str
import dryscrape

browserSpecs = 'Mozilla/5.0 (X11; Linux x86_64; rv:18.0) Gecko/20100101 Firefox/18.0 (compatible;)'
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-Agent', browserSpecs), ('Accept', '*/*')] # need ths to re-direct

# SEARCH A SITE FOR FORMS AND FORM CONTROLS----------------------------------------------------------------------
def find_search(site):
  br.open(site)
  index = 0
  for form in br.forms():
      print "----------FORM----------------------"
      print "Form name:", form.name, "Form index:", index
      # print form
      # print
      index +=1
      subindex = 0
      for control in form.controls:
        print "---------->>CONTROL----------------------"
        print "control name:", control.name, "control_index", index
        print "control type:", control.type
        subindex +=1


def find_articles_by_form(site, search_form_index, search_controler_name, search_term):
    br.open(site)
    br.select_form(nr=search_form_index)
    br.form[search_controler_name]=search_term
    result = br.submit()
    print result.read()
    print result.geturl()

def find_articles_by_url(search_url, slug):
  # result = br.open(search_url+slug)
  session = dryscrape.Session()
  session.visit(search_url+slug)
  eval_url = smart_str(session.url())
  html = session.body() 
  # print result.read()
  # print html
  soup = BeautifulSoup(html)
  a= soup.find("div", {"id": "searchResults"})
  print smart_str(a.prettify())

site = "http://www.nytimes.com"
search_url = "http://query.nytimes.com/search/sitesearch/?action=click&contentCollection&region=TopBar&WT.nav=searchWidget&module=SearchSubmit&pgtype=Homepage#/"
search_term = "texas is awesome"
# find_search(site)
# find_articles(site, 0, "search-input","texas is awesome")
find_articles_by_url(search_url, search_term)

