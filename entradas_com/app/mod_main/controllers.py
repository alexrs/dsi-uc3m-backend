# Import flask dependencies
from flask import Blueprint, render_template, redirect, request, make_response
from app.models import *
from app import db
import random

mod_main = Blueprint('main', __name__,)

# Set the route and accepted methods
@mod_main.route('/')
def index():
	return render_template("main/index.html")

@mod_main.route('/login/', methods=['POST'])
def login():
	print "Login"
	if request.cookie.get('username'):
		username = request.form['username']
		password = request.form['password']
		user = User.query.filter_by(username=username).first()
		if user.email == email:
			resp = make_response(render_template("main/index.html", user=user, saves=request.cookie.get('username')) )
			resp.set_cookie('user', str(username))
			return resp
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

