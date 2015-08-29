from bs4 import BeautifulSoup
from django.utils.encoding import smart_str
import re
import dryscrape

class NYTimes(BaseScraper):

  def iterable(soup):
    search_results = soup.find("div", {"id": "searchResults"})
    
    # return iterable
    return search_results.find_all('li', {'class':"story"}):

  def url(search_item):
    # url
    link = search_item.find('a', href=True)
    return link['href']

  def headline(search_item):
    # headline
    headline = search_item.find('span', {'class':"printHeadline"})
    #remove "Print Headline: " from headline
    info = re.search('"(.*)', smart_str(headline.contents[0])) 
    info = info.group(0)[1:-1]
    return info

  def author(search_item):
    # author
    author =  search_item.find('span', {'class':"byline"})
    #remove "By " from author info
    info = re.search('(By )(.*)', smart_str(author.contents[0]))
    info = info.group(2) 
    return info

  def date(search_item):
    # date
    date = search_item.find('span', {'class':"dateline"})
    return smart_str(date.contents[0]) 

  def summary(search_item): 
    # summary 
    summary = search_item.find('p', {'class':"summary"})
    info = ""
    #iterate through every line of summary contents
    for i in summary.contents:
      #skip formating tags embeded in summary info
      if re.match('<.*>', smart_str(i)) is None:
        info += smart_str(i).strip() + " "
    return info