from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm, RegisterForm
from feed.Feed import Feed

"""Make sure that crawler starts from last link and
	 works to first new in case of batch updates """

@app.route('/')
@app.route('/comic')
def comic():
    #title, description, link
    url_list = [ "http://www.questionablecontent.net/QCRSS.xml" \
		, "http://www.giantitp.com/comics/oots.rss" \
		, "http://xkcd.com/rss.xml" \
		, "http://twokinds.keenspot.com/rss.php" \
		, "http://feeds.feedburner.com/AvasDemon?format=xml"]
                    
    feed_list = [Feed(url) for url in url_list] 
    return render_template("comics.html", feeds = feed_list)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form = form)    

@app.route('/register')
def register():
    form = RegisterForm()
    return render_template('register.html', form = form)
