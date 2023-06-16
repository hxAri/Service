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

from service import service
from sqlalchemy import func


# Get SQLAlchemy instance.
sql = service.sql

# Represent Table Product.
class Product( sql.Model ):
	
	# Column to store the product ID.
	id = sql.Column( sql.String( 250 ), nullable=False, unique=True, primary_key=True )
	
	# Column to store the product name
	name = sql.Column( sql.String( 250 ), nullable=False )
	
	# Column to store the product price
	price = sql.Column( sql.BigInteger, nullable=False )
	
	# Column to store the product quantity
	quantity = sql.Column( sql.Integer, default=0, nullable=False )
	
	# Column to store the product creation date
	created = sql.Column( sql.Date(), server_default=func.now() )
	
	# Column to store the product update date
	updated = sql.Column( sql.Date(), server_default=func.now() )
	
	#[Product.__repr__()]: String
	def __repr__( self ):
		return f"<Product id=\"{self.id}\" name=\"{self.name}\" price={self.price} quantity={self.quantity} created=\"{self.created}\" updated=\"{self.updated}\" />"
	
	#[Product.dict()]: String
	def dict( self ):
		return {
			"id": self.id,
			"name": self.name,
			"price": self.price,
			"quantity": self.quantity,
			"createdAt": str( self.created ),
			"updatedAt": str( self.updated )
		}
	
