import urllib2
from Entry import Entry
from bs4 import BeautifulSoup

class Feed():

    def __init__(self, url, feed_type="xml"):
        try:
            f = urllib2.urlopen(url)
        except urllib2.HTTPError, e:
            print e.fp.read()
        #f = urllib2.urlopen(url)
        #page = BeautifulSoup(urllib2.urlopen(url), feed_type)
        page = BeautifulSoup(f, feed_type)
        self.title = page.find("title")
        items = page(["item", "entry"], limit = 5)
        self.entries = [Entry(item) for item in items]

    def get_last(self):
        return self.entries[0]
