from app import db

class User(db.Model):
    id = db.Column(db.Integer, Primary_key = True)
    name = db.Column(db.String(64), index = True, unique = True)
#    password = db.Column(db.

class Comic(db.Model):
    id = db.Column(db.Integer, Primary_key = True)
    title = db.Column(db.String(128), index = True, unique = True)
#put rest of comic db fields here
