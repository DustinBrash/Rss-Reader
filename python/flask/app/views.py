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
	url_list = [ "http://www.questionablecontent.net/QCRSS.xml" \
		, "http://www.giantitp.com/comics/oots.rss" \
		, "http://xkcd.com/rss.xml" \
		, "http://twokinds.keenspot.com/rss.php" \
		, "http://feeds.feedburner.com/AvasDemon?format=xml"]
                    
	feed_list = [Feed(url) for url in url_list] 
	return render_template("comics.html", feeds = feed_list)
