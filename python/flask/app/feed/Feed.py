import urllib2
from Entry import Entry
from bs4 import BeautifulSoup

class Feed():

    def __init__(self, url,):
	request = urllib2.Request(url)
        opener = urllib2.build_opener()
	request.add_header('User-Agent', "Chrome/44.0.2403.155" + 
		"+Rss Subscription Feed")
	f = opener.open(request).read()
	page = BeautifulSoup(f)
        self.title = page.find("title").string
        items = page(["item", "entry"], limit = 5)
        self.entries = [Entry(item) for item in items]

    def get_last(self):
        return self.entries[0]
