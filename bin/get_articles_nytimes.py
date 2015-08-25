from bs4 import BeautifulSoup
from django.utils.encoding import smart_str
import re
import dryscrape

def find_articles_by_url(search_url1, slug, search_url2="", page="", search_url3=""):
  # form address
  address = search_url1+slug+search_url2+str(page)+search_url3
  # print address

  # render html with dryscrape
  session = dryscrape.Session()
  session.visit(address)
  eval_url = smart_str(session.url())
  html = session.body() 

  # create html soup
  soup = BeautifulSoup(html)
  search_results = soup.find("div", {"id": "searchResults"})
  
  # parse articles
  for x in search_results.find_all('li', {'class':"story"}):
    
    # url
    link = x.find('a', href=True)
    print link['href']
    
    # headline
    try:
      headline = x.find('span', {'class':"printHeadline"})
      info = re.search('"(.*)', smart_str(headline.contents[0])) 
      info = info.group(0)[1:-1]
      print info
    except Exception as e:
      print e

    # author
    try:
      author =  x.find('span', {'class':"byline"})
      info = re.search('(By )(.*)', smart_str(author.contents[0]))
      info = info.group(2) 
      print info
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
search_term = "rand+paul"
search_url2 = "/since1851/allresults/"
page = 2
search_url3 = "/allauthors/newest/"

find_articles_by_url(search_url1, search_term, search_url2, page, search_url3)


