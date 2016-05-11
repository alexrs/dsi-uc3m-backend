from flask import Blueprint, render_template, request, make_response, session
from app.models import *
from app import db

mod_search = Blueprint('search', __name__,)


@mod_search.route('/search/', methods=['POST'])
def search():
	query = request.form['query']
	events = query_by_event_name(query)
	redirectTo = "search/search-results.html"
	if len(events)==1:
		event = query_by_id(events[0].id)
		print "\n\n\n %d \n\n\n\n", event.eventId
		result = event_genre(event.eventId)
		genres_list = ""
		if len(result) > 0:
			genres_list = ", ".join(result) if len(result) > 1 else result[0]
		result = [] #event_director(id)
		director = ""
		if len(result) > 0:
			director = ", ".join(result) if len(result) > 1 else result[0]

		result = [] #event_cast(id)
		cast = ""
		if len(result) > 0:
			cast = ", ".join(result) if len(result) > 1 else result[0]
                if 'username' in session:
                    user = session['username']
                    return render_template("event/event.html", event=event, genres_list=genres_list, director = director, cast = cast, user=user) 
                else:
                    return render_template("event/event.html", event=event, genres_list=genres_list, director = director, cast = cast) 
	else:
		if request.cookies.get('busqueda'):
			value = str(request.cookies.get('busqueda') + ',' + str(query))
		else:
			value = str(query)
		if 'username' in session:
			user = session['username']
			resp = make_response(render_template("search/search-results.html", query=query, events=events, user=user))
		else:
			resp = make_response(render_template("search/search-results.html", query=query, events=events))
			resp.set_cookie('busqueda', value)
		return resp

# http://flask-sqlalchemy.pocoo.org/2.1/queries/
def query_by_event_name(look_for):
	result = Event.query.filter(Event.title.like("%" + look_for + "%")).all()
	if result:
		return result
	else:
		return []

def query_by_id(id):
        result = Event.query.filter(Event.id==id).first()
        if result:
                return result
        else:
                return None
def event_genre(id):
    genre_list = Genre.query.filter_by(event_id=id).all()
    result = []
    for i in genre_list:
        genre = i.name.strip()
        if genre:
            result.append(genre)

    if len(result) > 1:
        return list(set(result))
    else:
        return []

def event_director(id):
    directors = db.session.query(movie_director).filter_by(event_id=id).all()
    print "here \n\n\n\n\n HERE"
    result = []

    for director in directors:
        director_name = CrewMember.query.filter_by(id=director[1]).first()
        if director_name.firstName.strip():
            result.append(director_name.firstName.strip())

    return list(set(result[:2]))

def event_cast(id):

    cast = db.session.query(movie_actor).filter_by(event_id=id).all()
    result = []

    for actor in cast:
        actor_name = Actor.query.filter_by(id=actor[1]).first()
        new = actor_name.firstName.strip()
        if new:
            result.append(new)

    return result[:3]

