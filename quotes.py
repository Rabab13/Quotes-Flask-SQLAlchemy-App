
# adding the request object and redirect and url_for to redirect to sepcific url
import os
import re
from flask import Flask ,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

app = Flask(__name__)
# comment out our local database after conected heruko database 
# app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:0000@localhost/quote'
# uri = os.getenv("DATABASE_URL")  # or other relevant config var
# if uri.startswith("postgres://"):
#     uri = uri.replace("postgres://", "postgresql://", 1)
# rest of connection code using the connection string `uri`
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://uvqtrsvpqkgowm:62ebde469f2747b4171fd52b175d65b30300a5f632bedcd8c003ab2a836cfc9d@ec2-18-215-111-67.compute-1.amazonaws.com:5432/d42cekce03urar'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)


# Create database tables 

class Quotes(db.Model):
	id = db.Column(db.Integer, primary_key= True)
	author = db.Column(db.String(30))
	quote = db.Column(db.String(2000))


# Create Routes 
@app.route('/')
def index():
	# Will call all data recorded into Quote table 
	result = Quotes.query.all()
# quote is the variable will use it in html file 
# calling variable fruits = to list name fruits 
	return render_template('index.html', result = result)



@app.route('/quotes')
# This the veiw function will call it as the route
def quotes():
	return render_template('quotes.html')

# add HTTP method 
@app.route('/process', methods = ['POST'])
# This the veiw function will call it as the route
def process():
	# Create 2 variable to store the data from the form 
	author = request.form['author']
	quote = request.form['quote']
	# Create variable to present the data which have 2 paramaters author and quote 
	quotedata = Quotes(author = author, quote = quote)
	db.session.add(quotedata)
	db.session.commit()
	# Will redirect the user to index.html which is the home page
	return redirect(url_for('index'))