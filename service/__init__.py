#!/usr/bin/env python
#encoding: utf-8

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

from datetime import date, datetime
from flask import jsonify, request, Response, render_template as render
from json import dumps
from sqlalchemy.orm.exc import NoResultFound

from . import service
from service.product import Product


app = service.app
run = service.app.run
sql = service.sql

# Allow debugable
debug = True

def stack( e ):
	return "{}: {} in file {} on line {}".format( type( e ).__name__, str( e ), e.__traceback__.tb_frame.f_code.co_filename, e.__traceback__.tb_lineno )

def catch( message, status, code ):
	return Response( **{
		"response": dumps( indent=4, obj={
			"message": message,
			"status": status,
			"code": code
		}),
		"headers": {
			"Content-Type": "application/json"
		},
		"status": code
	})

def result( data ):
	if isinstance( data, Product ):
		data = data.dict()
	if isinstance( data, dict ):
		for idx, key in enumerate( data ):
			if isinstance( data[key], datetime ):
				data[key] = str( data[key] )
	elif isinstance( data, list ):
		for idx, val in enumerate( data ):
			if isinstance( val, Product ):
				data[idx] = data[idx].dict()
			if isinstance( val, dict ):
				for i, k in enumerate( val ):
					if isknstance( val[k], datetime ):
						data[idx][k] = str( val[k] )
	return Response( **{
		"response": dumps( indent=4, obj={
			"status": "ok",
			"code": 200,
			"data": data
		}),
		"headers": {
			"Content-Type": "application/json"
		},
		"status": 200
	})

@app.errorhandler( 404 )
def pageNotFound( error=None ):
	return catch( "Page not found", "fail", 404 )

@app.errorhandler( 405 )
def methodNotAllowed( error=None ):
	return catch( f"Method {request.method} not allowed", "fail", 405 )

@app.route( "/", methods=[ "GET" ] )
def index():
	
	"""
	Home page, use this for try this Service.
	
	:return Render
	"""
	
	return render( "index.html" )

@app.route( "/api/products", methods=[ "GET" ] )
def display():
	
	"""
	Display all products.
	
	:return Response
		Instance of class Response
	"""
	
	return result( Product.query.all() )

@app.route( "/api/products", methods=[ "POST" ] )
def insert():
	
	"""
	Create or insert new product.
	
	:return Response
		Instance of class Response
	"""
	
	if  request.headers.get( "Accept" ) != "application/json" or \
		request.headers.get( "Content-Type" ) != "application/json":
		return catch( "Invalid header", "fail", 400 )
	data = request.get_json()
	if  "id" not in data or \
		"name" not in data or \
		"price" not in data or \
		"quantity" not in data:
		return catch( "Invalid request body", "fail", 400 )
	if  int( data['price'] ) <= 0:
		return catch( "Invalid request body", "fail", 400 )
	try:
		try:
			product = Product( **data )
		except Exception as e:
			return catch( "Invalid request body", "fail", 400 )
		sql.session.add( product )
		sql.session.commit()
		return result( product )
	except Exception as e:
		return catch( stack( e ) if debug else "Something wrong", "fail", 503 )
	

def select( id ):
	
	"""
	Select product record from database.
	
	:params String id
		Product id
	:return Product
		Instance of class Represent Product
	"""
	
	return Product.query.filter_by( id=id ).one()
	

def single( id ):
	
	"""
	Get single product.
	
	:params String id
		Product id
	:return Response
		Instance of class Response
	"""
	
	return result( select( id ) )
	

def update( id ):
	
	"""
	Handle update product data.
	
	:params String id
		Product id
	:return Response
		Instance of class Response
	"""
	
	data = request.get_json()
	product = select( id )
	if  "name" not in data or \
		"price" not in data or \
		"quantity" not in data:
		return catch( "Invalid request body", "fail", 400 )
	if  int( data['price'] ) <= 0:
		return catch( "Invalid request body", "fail", 400 )
	else:
		product.name = data['name']
		product.price = data['price']
		product.quantity = data['quantity']
		product.updated = date.today()
	try:
		sql.session.commit()
	except Exception as e:
		return catch( stack( e ) if debug else "Something wrong", "fail", 503 )
	return result( product )
	

def delete( id ):
	
	"""
	Handle delete product.
	
	:params String id
		Product id
	:return Response
		Instance of class Response
	"""
	
	product = select( id )
	try:
		sql.session.delete( product )
		sql.session.commit()
	except Exception as e:
		return catch( stack( e ) if debug else "Something wrong", "fail", 503 )
	return Response( **{
		"response": dumps( indent=4, obj={
			"status": "ok",
			"code": 200
		}),
		"headers": {
			"Content-Type": "application/json"
		},
		"status": 200
	})
	

@app.route( "/api/products/<id>", methods=[ "GET", "PUT", "DELETE" ] )
def handle( id ):
	
	"""
	Handle requests to retrieve, update, and delete products.
	
	:params String id
		Product id
	:return Response
		Instance of class Response
	"""
	
	try:
		match request.method:
			case "GET":
				return single( id )
			case "PUT":
				return update( id )
			case "DELETE":
				return delete( id )
			case _:
				return methodNotAllowed()
	except NoResultFound:
		return pageNotFound()
	
