from app import db
from werkzeug import generate_password_hash, check_password_hash
import datetime

class User(db.Model):
    uid = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True)
    pwd_hash = db.Column(db.String(54))
    email = db.Column(db.String(120), unique = True)
    comics = db.Column(db.PickleType())

    def __init__(self, name, email, password):
        self.name = name.title()
        self.email = email.lower()
        self.set_password(password)
        self.comics = []

    def set_password(self, password):
        self.pwd_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pwd_hash, password)

    def __repr__(self):
        return "<User %r>" % self.name

class Comic(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    feed_link = db.Column(db.Text(), unique = True)
    last_updated = db.Column(db.String(128))
    last_checked = db.Column(db.DateTime())
    last_unread = db.Column(db.Text())

    def __init__(self, link):
        self.last_updated = datetime.min
        self.feed_link = link
        self.last_updated = datetime.min
