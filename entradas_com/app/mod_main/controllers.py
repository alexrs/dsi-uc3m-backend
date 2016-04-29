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
	print "Login"
	username = request.form['username']
	password = request.form['password']
	user = User.query.filter_by(username=username).first()
	if user.email == email:
		return render_template("main/index.html", user=user)
	return render_template("main/index.html")

@mod_main.route('/signup/', methods=['POST'])
def signup():
	print "Sign up"
	username = request.form['username']
	email = request.form['email']
	password = request.form['password']
	user = User(username, email, password)

	db.session.add(user)
	db.session.commit()
	return render_template("main/index.html", user=user)

def get_suggestions():
	pass


