import urllib2
import datetime
from Entry import Entry
from bs4 import BeautifulSoup

class Feed():

    def __init__(self, url):
        #create urllib object for reading source
	request = urllib2.Request(url)
	#pass in an Auth-User because some rss feeds are jerks :(
        opener = urllib2.build_opener()
	request.add_header('User-Agent', "Chrome/44.0.2403.155" + 
		"+Rss Subscription Feed")
	f = opener.open(request).read()
	#pass source to BS for parsing
	page = BeautifulSoup(f)
        self.title = page.find("title").string
        items = page(["item", "entry"], limit = 10)
        self.entries = [Entry(item) for item in items]
        #checked update every time
        #compare last_link, if diff update link and last_updated
        #actual check higher up
        self.last_updated = datetime.utcnow()
        self.last_checked = self.last_updated
        self.last_link = None if len(self.entries) == 0 else self.entries[0]

    def get_last(self):
        return self.entries[0]
