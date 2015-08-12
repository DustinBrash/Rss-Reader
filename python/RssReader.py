import urllib2, MySQLdb, datetime
from bs4 import BeautifulSoup

"""Updates comic entries in db iff last build date and link has changed"""

def update_comic(url):
#   initialize database access and web page source in BeautifulSoup
    page, master_tag, comic_cursor = setup(url, "comic-db")
#   use the title to check for changes
    comic_title = master_tag.item.title.string
    comic_cursor.execute("""SELECT last_build_date FROM
        comics WHERE title = %s""", comic_title)
#   Need to check to see what SQL returns on an unpopulated entry
    if last_build_date is not build_date_from_db:
        last_link = master_tag.item.link.string
        link_from_db = comic_cursor.execute("""SELECT link FROM comics WHERE
            title = %s""", comic_title)
        link_updated = datetime.now()
#       Update values from if statement here        
    last_update_check = datetime.now()

def add_comic(url):
    page, master_tag, cursor = setup(url, "comic-db")
    series_title = master_tag.title.string
    #check for comic title in DB, add elements
    cursor.execute("""SELECT series_title FROM comics""")
#   Does fetchall return a tuple consisting of just strings
#   or a muliti-dimensional tuple?
    found = False
    while not found and (row = cursor.fetchone()) is not None:
        found = series title is row[0]
    if not found:
        cursor.execute("""INSERT INTO comics (SeriesTitle, LastComic,
            LastComicLink, LinkUpdated, LastUpdateCheck)""")
    
"""Reads a supplied URL, in this case the
    source code of the RSS feed is needed
    as a Soup"""
def read(url):
    return BeautifulSoup(urllib2.urlopen(url), 'xml')

def setup(url, database_name):
    page = read(url)
    master_tag = page.rss.channel
    db = MySQLdb.connect(user = "dbmanager", db = database_name)
    cursor = comic_db.cursor()
    return page, master_tag, cursor
