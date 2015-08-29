from bs4 import BeautifulSoup
from django.utils.encoding import smart_str
import re
import dryscrape

def get_contents(url):

  # render html with dryscrape
  session = dryscrape.Session()
  session.visit(url)
  eval_url = smart_str(session.url())
  html = session.body() 

  # create html soup
  soup = BeautifulSoup(html)
    
  # headline
  try:
    headline = soup.find('h1', {'class':"story-heading"})
    print headline.contents[0]
  except Exception as e:
    print e

  # author
  try:
    author =  soup.find('span', {'class':"byline-author"})
    print author.contents[0]
  except Exception as e:
    print e
    
  # date
  try:
    date = soup.find('time', {'class':"dateline"})
    print date.contents[0]
  except Exception as e:
    print e
    
  # story 
  try:
    for content in soup.find_all('p', {'class':"story-body-text"}):
      print smart_str(content.contents[0])
  except Exception as e:
    print e

  print " "

url = "http://www.nytimes.com/2015/08/27/business/dealbook/daily-stock-market-activity.html?ribbon-ad-idx=3&rref=homepage&module=Ribbon&version=origin&region=Header&action=click&contentCollection=Home%20Page&pgtype=article"

get_contents(url)


