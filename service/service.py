#!/usr/bin/env python

#
# @author Ari Setiawan
# @create 15.06-2023
# @github https://github.com/hxAri/Service
#
# Service Copyright (c) 2022 - Ari Setiawan <hxari@proton.me>
# Service Licence under GNU General Public Licence v3
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path


# Create a dynamic folder name for the template.
folder = "template"
folder = path.join( path.dirname( __file__ ), folder )

# Initiliazie flask instance.
app = Flask( __name__, template_folder=folder )

# Set SQLAlchemy configurations.
app.config['SQLALCHEMY_TRACT_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root@localhost:3306/store"

# Initialize SQLAlchemy.
sql = SQLAlchemy( app )
