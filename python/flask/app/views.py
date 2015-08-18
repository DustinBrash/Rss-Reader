from app import app
from flask import render_template
#import feed

"""Make sure that crawler starts from last link and
	 works to first new in case of batch updates """

@app.route('/comic')
def comic():
	#title, description, link
	entries = [{"title": "My Comic", "description" : "A Comic I Made Up Just Now", "link" : "httP://www.google.com"}]
	entries = entries * 5 
	return render_template("comics.html", entries=entries)
