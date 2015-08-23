import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'users.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repositry')

#CSRF Form stuff
WTF_CSRF_ENABLED = True
#change later
SECRET_KEY = 'password'
