# Import flask dependencies
from flask import Blueprint, render_template, redirect
from app.models import *
from app import db

mod_main = Blueprint('main', __name__,)

# Set the route and accepted methods
@mod_main.route('/')
def index():
	return render_template("main/index.html")

@mod_main.route('/login/')
def login():
	username = request.form['username']
	password = request.form['password']
	user = User.query.filter_by(username=username).first()
	if user.email == email:
		#do login
		pass

@mod_main.route('/signin/')
def signin():
	username = request.form['username']
	email = request.form['email']
	password = request.form['password']
	user = User(username, email, password)

	db.session.add(user)
	db.session.commit()

	

def get_suggestions():
	pass


