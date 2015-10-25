# election_sentiment
The purpose of this project is two-fold:
1. Teach others how to code through an interesting project that uses db, orms, webscraping, analysis libraries, modern web frameworks, etc..
2. Create a sentiment analyzer for presidential hopefuls based of media reports 

## Objective: 

1. Monitor a set of media sites (such as the top 10 broadcast news outlets by traffic)
2. Whenever an article is published about a presediential canidate, download the article
3. Scan the article using a sentiment analysis tool
4. Display the results of sentiment change over time for different news outlets
5. Add correlations to election events

## Technical Outline:

The project has three distinct phases:

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

## Git Workflow:

![Workflow for new project contributors](/img/git_workflow.png)

## Documentation Standards



## Development Environment

#### Overview

A big problem with projects involving more than one person is being consistent about which versions of third party code (libraries) and programming languages are used. One easy way to solve this problem is with a virtual environment. 

#### Example 

The necessity of a virtual environment can easily be seen with the differences between Python 2 and Python 3. Python 3 is not backwards compatible with Python 2. Thus, trying to run Python 2 code using Python 3 wont work. 
Backwards compatibility is not always preserved with major release upgrades. If a project follows [Semantic versioning](http://semver.org/) aka Major.Minor.Patch numbering (like 2.1.0). The Major version number repressents a backwards incompatible update. Minor version represents a backwards compatible update. Patch is a backwards-compatible bug fix. 

#### Solution: Virtual Environments

A virtual environment module (named [Venv](https://docs.python.org/3/library/venv.html) is included by default in Python 3. [Python-guide.org](http://docs.python-guide.org/en/latest/dev/virtualenvs/) has a pretty good and simple outline on how to use it. 

#### Venv Cheatsheet

1) Use virtualenv to make sure versioning and dependencies of python and required libraries are correct

`$ source my_project/venv/bin/activate`

2) Virtualenv should be loaded from the requriements.txt. This gets rid of hardcoding issues and makes it so we don't have to sync libaries over github.

`$ pip install -r requirements.txt`

3) When you make a change to any dependency, you should freeze the current state of the environment packages and regenerate the requirements.txt file

`$ pip freeze > requirements.txt`

## TODO

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

