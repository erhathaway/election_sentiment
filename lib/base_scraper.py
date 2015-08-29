class BaseScraper():
  """Extendable scraper object used to scrape websites"""

  def __init__(self):
    self.data = []

  def search_template(url):
    raise NotImplementedError

  def content_template(url):
    raise NotImplementedError

  @classmethod
  def store_search(source_object, canidate_object):
    pass

  @classmethod
  def store_content():
    pass

  def get_searches(self, source_object, canidate_object, start_page, max_duplicates=10):
    page = start_page
    for canidate in canidates:
      search_template(canidate)

  def get_content(self):
    pass