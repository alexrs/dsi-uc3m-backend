# Import flask dependencies
from flask import Blueprint, render_template, redirect, request, make_response, session
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
			event.append(Event.query.filter(Event.title.like("%" + busquedas_list[i] + "%")).with_entities(Event.eventId).first())
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
			while len(recomendacion)<3:
				rec = Event.query.filter(Event.eventId.like("%" + str(ids[int(random.random()*len(ids))][0]) + "%")).first()
				if len(rec.imdb)>0:
					recomendacion.append(Event.query.filter(Event.eventId.like("%" + str(ids[int(random.random()*len(ids))][0]) + "%")).first())
					
			return recomendacion
		else:
			return None

def get_random_suggestions():
	random_suggestions = []
	while len(random_suggestion)<4:
		ran_sug = Event.query.get(int(random.random()*len(random_suggestion)*100))
		if len(ran_sug.imdb)>0:
			random_suggestions.append(ran_sug)
	return random_suggestions

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
		random_suggestions = get_random_suggestions()
		return render_template("main/index.html", suggestions=random_suggestions[1:4])
	else:
		if len(suggestions)==1:
			for i in range(2):
				suggestions.append(Event.query.get(int(random.random()*i*100)))

		elif len(suggestions)==2:
			suggestions.append(Event.query.get(int(random.random()*i*100)))
	if 'username' in session:
		user = session['username']
		return render_template("main/index.html", suggestions=suggestions, user=user)
	else:
		return render_template("main/index.html", suggestions=suggestions)

@mod_main.route('/login/', methods=['POST'])
def login():
	print "Login"
	username = request.form['email']
	password = request.form['password']
	user = User.query.filter_by(email=username).first()
	if user.email == username:
		session['username'] = user.username
		return render_template("main/index.html", user=user, username=user.username)


@mod_main.route('/signup/', methods=['POST'])
def signup():
	print "df"
	username = request.form['username']
	print username
	password = request.form['password']
	print password
	email = request.form['email']

	user = User(username, email, password)

	db.session.add(user)
	db.session.commit()
	return render_template("main/index.html", user=user)

@mod_main.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('index'))
