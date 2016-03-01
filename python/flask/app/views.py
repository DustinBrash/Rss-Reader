from app import app
from flask import render_template
from feed.Feed import Feed
import os

"""Make sure that crawler starts from last link and
	 works to first new in case of batch updates """

@app.route('/')
@app.route('/comic')
def comic():
    #title, description, link
    file_name = os.path.join(os.path.dirname(__file__), 'sites.txt')
    with open(file_name) as f:
    	url_list = f.readlines()
        print(str(url_list))
   	feed_list = [Feed(url) for url in url_list] 
    	return render_template("comics.html", title = "Comics", feeds = feed_list)

