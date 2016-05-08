# Import flask dependencies
from flask import Blueprint, render_template, redirect, request, make_response
from app.models import *
from app import db
from collections import Counter
import random

mod_main = Blueprint('main', __name__,)

#Parsea las cookies de busqueda, separadas por un 54, o devuelve una lista vacia
def parse_search_cookies():
	searchCookies = request.cookies.get('busqueda')
	if searchCookies:
		searchCookies.split("\54")
		return searchCookies
	else:
		return []

"""
 Busca en las cookies, coge los ids de los eventos que salgan de una query con los ultimos
 resultados de busqueda, y usa esos ids para buscar el genero mas buscado
 una vez tiene el genero mas buscado por el usuario, hace una busqueda en genres sobre ese
 genero, de peliculas ( .all() ), y selecciona 3 al azar.
 
"""
def get_suggestions():
	busquedas = parse_search_cookies()
	result = []
	if len(busquedas)==0:
		return None
	else:
		busquedas_list = busquedas.split(',')
		event = []
		similar = []
		recomendacion = []
		for i in range(len(busquedas_list)):
			event = Event.query.filter(Event.title.like("%" + busquedas_list[i] + "%")).with_entities(Event.eventId).all()
			if event:
				genres = []
				for j in range(len(event)): 
					genres.append(Genre.query.filter(Genre.event_id.like("%" + str(event[j][0]) + "%")).with_entities(Genre.name).all() ) 
				ocurrencias = []
				ocurrenciasIndex = []
				for i in range(len(genres)):
					if genres[i][0] not in ocurrencias:
						ocurrencias.append(genres[i][0])
						ocurrenciasIndex.append(1)
					else:
						ocurrenciasIndex[ocurrencias.index(genres[i][0])] += 1
				
				similar = ocurrencias[ocurrenciasIndex.index(max(ocurrenciasIndex))]
				ids = Genre.query.filter(Genre.name.like("%" + similar[0][0] + "%")).with_entities(Genre.event_id).all()	
				for k in range(3):	
					recomendacion.append(Event.query.filter(Event.eventId.like("%" + str(ids[int(random.random()*len(ids))][0]) + "%")).first())
				return recomendacion
				
			else: 
				return None
		return None


# Set the route and accepted methods
"""
 Recoge sugerencias con get_suggestions, en caso de no haber, devuelve 3 busquedas
 al azar. Si hay, pero es una sola, se le agnaden dos al azar, y si son dos, se le agnade una

"""
@mod_main.route('/')
def index():
	suggestions = get_suggestions()
	print suggestions
	if not suggestions:
		random_suggestions = []
		for i in range(4): #por alguna rara razon, el primer resultado de random_suggestions 
				   #me sale None siempre
			random_suggestions.append(Event.query.get(int(random.random()*i*100)))
		return render_template("main/index.html", suggestions=random_suggestions[1:4])
	else:
		if len(suggestions)==1:
			for i in range(2):
				suggestions.append(Event.query.get(int(random.random()*i*100)))
		
		elif len(suggestions)==2:
			suggestions.append(Event.query.get(int(random.random()*i*100)))
	
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


