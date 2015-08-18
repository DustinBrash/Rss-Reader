import urllib2
from bs4 import BeautifulSoup

class feed():

    def __init__(self, url, feed_type="xml", tag_in="item"):
        self.page = BeautifulSoup(urllib2.urlopen(url), feed_type)
        self.master_tag = self.page.rss.channel
        self.tag = tag_in

    def __repr__(self):
        return self.master_tag.title.string + ": " + self.master_tag.description.string
        
    def get_item(self, index):
        return self.master_tag.find_all(self.tag)[index]

    def get_item_range(self, a, b):
        return self.master_tag.find_all(self.tag)[a : b]

    def get_item_head(self):
        return self.master_tag.item    

    def get_tag_result(self, field, function):
        ret = function.find(field).string if type(function) is not list else \
              [tag.find(field).string for tag in function]
        return ret
