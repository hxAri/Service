
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

# Create a dynamic folder name for the template.
folder = "service/template"
folder = path.join( path.dirname( __file__ ), folder )

# Initiliazie flask instance.
app = Flask( __name__, template_folder=folder )

# Set SQLAlchemy configurations.
app.config['SQLALCHEMY_TRACT_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root@localhost:3306/store"

# Initialize SQLAlchemy.
db = SQLAlchemy( app )
