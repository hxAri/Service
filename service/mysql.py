
from flask_sqlalchemy import SQLAlchemy
from service import app

db = SQLAlchemy( app.app )
