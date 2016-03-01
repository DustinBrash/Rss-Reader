from app import app
from flask import render_template
from feed.Feed import Feed

"""Make sure that crawler starts from last link and
	 works to first new in case of batch updates """

@app.route('/')
@app.route('/comic')
def comic():
    #title, description, link
    with open("sites.txt") as f:
    	url_list = f.readlines()
   	feed_list = [Feed(url) for url in url_list] 
    	return render_template("comics.html", title = "Comics", feeds = feed_list)

