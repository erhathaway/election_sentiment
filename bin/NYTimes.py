import os, sys

#first change the cwd to the script path
scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
os.chdir(scriptPath)

#append the relative location you want to import from
sys.path.append("../lib")

from base_scraper import BaseScraper

from django.utils.encoding import smart_str
import re

class NYTimes(BaseScraper):

  def iterable(self, soup):
    search_results = soup.find("div", {"id": "searchResults"})
    # return iterable
    items = search_results.find_all('li', {'class':"story"})
    return items

  def get_url(self, search_item):
    # url
    link = search_item.find('a', href=True)
    return link['href']

  def get_headline(self, search_item):
    # headline
    headline = search_item.find('span', {'class':"printHeadline"})
    #remove "Print Headline: " from headline
    info = re.search('"(.*)', smart_str(headline.contents[0])) 
    info = info.group(0)[1:-1]
    return info

  def get_author(self, search_item):
    # author
    author =  search_item.find('span', {'class':"byline"})
    #remove "By " from author info
    info = re.search('(By )(.*)', smart_str(author.contents[0]))
    info = info.group(2) 
    return info

  def get_date(self, search_item):
    # date
    date = search_item.find('span', {'class':"dateline"})
    return smart_str(date.contents[0]) 

  def get_summary(self, search_item): 
    # summary 
    summary = search_item.find('p', {'class':"summary"})
    info = ""
    #iterate through every line of summary contents
    for i in summary.contents:
      #skip formating tags embeded in summary info
      if re.match('<.*>', smart_str(i)) is None:
        info += smart_str(i).strip() + " "
    return info