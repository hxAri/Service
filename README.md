# Service
## About
Web Service Rest API with Flask, it's really very simple, and no hassle

## Features
* Interactive home page for testing
* It supports API specifications
* JSON response resource

## Requests
* `GET /` Show main page
* `GET /api/products` Get all products
* `GET /api/products/<id>` Get product by id
* `PUT /api/products/<id>` Update product info
* `POST /api/products` Create new product
* `DELETE /api/products/<id>` Delete product by id

# Installation
* First of all, please download this repository archive file or clone directly using git
* Then import the sql script in the `storage.sql` file to your mysql database engine
* Then install all the required modules in the requirements.txt file with `pip install -r requirements*`
* Once everything is done run the main script which resides in the root of the project with `python main*` this will open a local connection with port 8080
* Then open your favorite browser and go to `http://127.0.0.1:8080` there you go!

## Licence
All source code for this project is licensed under the GNU General Public License v3. Please [see](https://www.gnu.org/licenses) the original document for more details.

