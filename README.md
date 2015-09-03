# election_sentiment
Sentiment analyzer for presidential hopefuls based of media reports 

### Objective: 

1. Monitor a set of media sites (such as the top 10 broadcast news outlets by traffic)
2. Whenever an article is published about a presediential canidate, download the article
3. Scan the article using a sentiment analysis tool
4. Display the results of sentiment change over time for different news outlets
5. Add correlations to election events

### Technical Details:

1. Web scraping
 - LXML and Beautiful Soup
 - SQLAlchemy 
    - Sqlite for development
    - Postgres for production

2. Data analysis
 - Simple trend analysis
 - etc...
 - Creation of JSON documments

3. Website
 - Deployment: Heroku
 - Framework: Flask
 - Visulization: D3.js
 - Database: Postgres using JSON Documents

### Workflow:

![Workflow for new project contributors](/img/git_workflow.png)


### TODO

#### Architecture

Move authors to EAV table (is this worth it if using heroku with row limitations???)


#### Errors

###### Unresolved errors:

O'Malley doesn't always match in headline when it should...

###### Resolved errors:

1. There are no search results: 

```
{"class":"InvalidResponseError","message":"Unable to load URL: http://query.nytimes.com/search/sitesearch/?action=click&contentCollection&region=TopBar&WT.nav=searchWidget&module=SearchSubmit&pgtype=Homepage#/elizabeth+WARREN/since1851/allresults/23/allauthors/newest/ because of error loading http://3951336.fls.doubleclick.net/activityi;src=3951336;type=digit0;cat=tier30;ord=4332975815050.3037?: Unknown error"}
Traceback (most recent call last):
  File "find_articles.py", line 33, in <module>
    nytimes.get_search_results(sources[0],canidate)
  File "/home/ethan/Dropbox/Programs/election_sentiment/lib/base_scraper.py", line 141, in get_search_results
    for search_item in self.iterable(soup):
  File "../bin/NYTimes.py", line 18, in iterable
    search_results = soup.find("div", {"id": "searchResults"})
AttributeError: 'NoneType' object has no attribute 'find'
```

