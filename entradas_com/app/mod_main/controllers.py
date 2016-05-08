# Import flask dependencies
from flask import Blueprint, render_template, redirect, request, make_response
from app.models import *
from app import db
import random

mod_main = Blueprint('main', __name__,)

#Parsea las cookies de busqueda, separadas por un 54, o devuelve una lista vacia
def parse_search_cookies():
	print "AQUIIIIIIIIIIIIIIII\n"
	searchCookies = request.cookies.get('busqueda')
	if searchCookies:
		searchCookies.split("\54")
		return searchCookies
	else:
		return []

#Busca en las cookies de busqueda, si no hay, devuelve los 3 primeros resultados
def get_suggestions():
	busquedas = parse_search_cookies()
	result = []
	if len(busquedas)==0:
		result = Event.query.filter().all()
		print "<<<<<<<<<< result  <>>>>>>>>>>>\n"
		print result
		print "\n"
		return result[:3]
	else:
		busquedas_list = busquedas.split(',')
		for i in range(len(busquedas_list)):
			result.append( Event.query.filter(Event.title.like("%" + busquedas_list[i] + "%")).first() ) 
		print "<<<<<<<<<< result  <>>>>>>>>>>>\n"
		print result
		print "\n"
		return result[len(result)-3:len(result)]


# Set the route and accepted methods
@mod_main.route('/')
def index():
	suggestions = get_suggestions()
	print "<<<<<<<<< suggestions >>>>>>>>>>>>>>>>>< "
	print suggestions
	print "\n"
	
	if not suggestions:
		random_suggestions = []
		for i in range(4):
			random_suggestions.append(Event.query.get(int(random.random()*i*100)))
		print "<<<<<<<<< random_suggestions >>>>>>>>>>>>>>>>>< "
		print random_suggestions
		print "\n"
		return render_template("main/index.html", suggestions=random_suggestions[1:4])
	return render_template("main/index.html", suggestions=suggestions)

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

