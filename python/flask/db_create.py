from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI as URI
from config import SQLALCHEMY_MIGRATE_REPO as REPO
from app import db
import os.path

db.create_all()
if not os.path.exists(REPO):
    api.create(REPO, 'database repository')
    api.version_control(URI, REPO)
else:
    api.version_control(URI, REPO, api.version(REPO))

