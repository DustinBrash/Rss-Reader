"""
    Format for database is as follows:
    SeriesTitle, LastComicTitle, LastComicLink, LinkUpdatedDate, LastUpdateCheck
"""

"""
    Eventually change behavior to archive last few comics
"""

import urllib2, sqlite3, datetime
from bs4 import BeautifulSoup

"""Updates comic entries in db iff last build date and link has changed"""

def update_comic(url):
#   initialize database access and web page source in BeautifulSoup
    master_tag, comic_cursor, connection = setup(url, "comic.db")
#   use the title to check for changes
    item = master_tag.item
    comic_title = item.title.string
    comic_cursor.execute("""SELECT last_build_date FROM
        comics WHERE title = ?""", (comic_title,))
#   Need to check to see what SQL returns on an unpopulated entry
    if comic_title is not comic_cursor.fetchone()[1]:
        last_link = item.link.string
        last_title = item.title.string
        link_updated = datetime.now()
#       Update values from if statement here
        connection.execute("""UPDATE comics SET LastComicTitle = ?,
            LastComicLink = ?, LinkUpdatedDate = ?
            WHERE SeriesTitle = ?""" (last_title, last_link,
                                      link_updated, comic_title))
#   Either way, update the LastUpdateCheck
    last_update_check = datetime.now()
    connection.execute("""UPDATE comics
                            SET LastUpdateCheck = ?
                            WHERE SeriesTitle = ?""",
                        (last_update_check, master_tag.title.string))
    connection.commit()
    connection.close()

def add_comic(url):
    master_tag, cursor, connection = setup(url, "comic.db")
    series_title = master_tag.title.string
#   check for comic title in DB, add elements
    cursor.execute("""SELECT series_title FROM comics""")
#   Does fetchall return a tuple consisting of just strings
#   or a muliti-dimensional tuple?
    found = False
    while not found and (row = cursor.fetchone()) is not None:
        found = series title is row[0]
    if not found:
        item = master_tag.item
        connection.execute("""INSERT INTO comics (SeriesTitle, LastComic,
            LastComicLink, LinkUpdatedDate, LastUpdateCheck)
            VALUES (?, ?, ?, ?, ?)""", (series_title,
                item.title.string, item.link.string
                datetime.now(), datetime.now()))
        connection.commit()
    connection.close()
    
"""Reads a supplied URL, in this case the
    source code of the RSS feed is needed
    as a Soup"""
def read(url):
    return BeautifulSoup(urllib2.urlopen(url), 'xml')

def setup(url, database_name):
    page = read(url)
    master_tag = page.rss.channel
    db = sqlite3.connect(database_name)
    cursor = comic_db.cursor()
    return master_tag, cursor, db
