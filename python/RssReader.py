import urllib2, MySQLdb
from bs4 import BeautifulSoup

def update_comic(url):
    page = read(url)    
    last_build_date = page.channel.lastBuildDate.string
#    build_date_from_db = "TEMP"
    comic_title = master_tag.item.title.string
    last_link = master_tag.item.link.string
#    link_updated = "NOW"
#    last_update_check = "NOW"

def add_comic(url):
    page = read(url)
    master_tag = page.rss.channel
    title = master_tag.title.string
    #check for comic title in DB, add elements

"""Reads a supplied URL, in this case the
    source code of the RSS feed is needed
    as a Soup"""
def read(url):
    return BeautifulSoup(urllib2.urlopen(url), 'xml')
