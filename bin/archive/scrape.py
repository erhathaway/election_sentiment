# import mechanize
from bs4 import BeautifulSoup
from django.utils.encoding import smart_str
import re
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