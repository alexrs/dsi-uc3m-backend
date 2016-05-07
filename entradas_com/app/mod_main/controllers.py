# Import flask dependencies
from flask import Blueprint, render_template, redirect, request
from app.models import *
from app import db

mod_main = Blueprint('main', __name__,)

# Set the route and accepted methods
@mod_main.route('/')
def index():
	return render_template("main/index.html")

@mod_main.route('/login/', methods=['POST'])
def login():
	email = request.form['email']
	password = request.form['password']
	user = User.query.filter_by(email=email).first()
	if user is not None:
		return render_template("main/index.html", user=user)
	return render_template("main/index.html")

@mod_main.route('/signup/', methods=['POST'])
def signup():
	print "Sign"
	email = request.form['email']
	username = request.form['username']
	password = request.form['password']
	user = User(username, email, password)

	db.session.add(user)
	db.session.commit()
	return render_template("main/index.html", user=user)

def get_suggestions():
	pass


