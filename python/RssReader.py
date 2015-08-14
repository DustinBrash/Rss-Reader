"""
    Format for database is as follows:
    SeriesTitle, LastComicTitle, LastComicLink, LinkUpdatedDate, LastUpdateCheck
"""

"""
    Eventually change behavior to archive last few comics
"""

import sqlite3, datetime, feed.feed


"""Updates comic entries in db iff last build date and link has changed"""

def update_comic(url):
#   initialize database access and web page source in BeautifulSoup
#   Different rss feeds use different conventions. Make some classes
#   to work with this
    feed, comic_cursor, connection = setup(url, "comic.db")
#   use the title to check for changes
    item = feed.get_item_head()
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
    feed, cursor, connection = setup(url, "comic.db")
    series_title = feed.master_tag.title.string
#   check for comic title in DB, add elements
    cursor.execute("""SELECT series_title FROM comics""")
#   Does fetchall return a tuple consisting of just strings
#   or a muliti-dimensional tuple?
    found = False
    while not found and (row = cursor.fetchone()) is not None:
        found = series title is row[0]
    if not found:
        item = feed.get_item_head()
        connection.execute("""INSERT INTO comics (SeriesTitle, LastComic,
            LastComicLink, LinkUpdatedDate, LastUpdateCheck)
            VALUES (?, ?, ?, ?, ?)""", (series_title,
                item.title.string, item.link.string
                datetime.now(), datetime.now()))
        connection.commit()
    connection.close()

def setup(url, database_name):
    feed = feed(url) 
    db = sqlite3.connect(database_name)
    cursor = comic_db.cursor()
    return feed, cursor, db
