from app import app
from flask import render_template
from feed.Feed import Feed

"""Make sure that crawler starts from last link and
	 works to first new in case of batch updates """

@app.route('/')
@app.route('/comic')
def comic():
	#title, description, link
	entries = [{"title": "My Comic", "description" : "A Comic I Made Up Just Now", "link" : "httP://www.google.com"}]
	entries = entries * 5
	url_list = ["http://www.giantitp.com/comics/oots.rss" \
                    , "http://www.questionablecontent.net/QCRSS.xml" \
                    , "http://twokinds.keenspot.com/rss.php"]
	feed_list = [Feed(url) for url in url_list] 
	return render_template("comics.html", feed_title = feed_list[0].title, \
                               entries = [x.get_last() for x in feed_list])
