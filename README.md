# election_sentiment
Sentiment analyzer for presidential hopefuls based of media reports 

### Objective: 

1. Monitor a set of media sites (such as the top 10 broadcast news outlets by traffic)
2. Whenever an article is published about a presediential canidate, download the article
3. Scan the article using a sentiment analysis tool
4. Display the results of sentiment change over time for different news outlets
5. Add correlations to election events

### Technically, this project has three parts

1. Web scraping
 - LXML and Beautiful Soup
 - SQLAlchemy w/ postgres

2. Data analysis
 - Simple trend analysis
 - etc...
 - Creation of JSON documments

3. Website
 - Flask
