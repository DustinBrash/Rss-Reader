from app import app
from flask import render_template
from feed.Feed import Feed

"""Make sure that crawler starts from last link and
	 works to first new in case of batch updates """

@app.route('/')
@app.route('/comic')
def comic():
    #title, description, link
    url_list = [ "http://www.questionablecontent.net/QCRSS.xml" \
		, "http://dailyderp.tumblr.com/rss" \
		, "http://www.nerdragecomic.com/feed.xml" \
		, "http://chaoslife.findchaos.com/feed" \
		, "http://lilmissrarity.com/rss" \
		, "http://studentofthenight.tumblr.com/rss" \
		, "http://www.alicegrove.com/rss" \
		, "http://feeds.feedburner.com/rsspect/fJur?format=xml" \
		, "http://www.smbc-comics.com/rss.php" \
		, "http://www.giantitp.com/comics/oots.rss" \
		, "http://xkcd.com/rss.xml" \
		, "http://twokinds.keenspot.com/rss.php" \
		, "http://feeds.feedburner.com/AvasDemon?format=xml"]
                    
    feed_list = [Feed(url) for url in url_list] 
    return render_template("comics.html", title = "Comics", feeds = feed_list)

