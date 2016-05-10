# Import flask dependencies
from flask import Blueprint, render_template, redirect, request
from app.models import *
from app import db

mod_event = Blueprint('event', __name__,)

# Set the route and accepted methods
@mod_event.route('/event/<id>')
def event(id):
	#return id
	event = query_by_id(id)
	if 'username' in session:
		user = session['username']
		return render_template("event/event.html", event=event, user=user)
	else:
		return render_template("event/event.html", event=event)

# http://flask-sqlalchemy.pocoo.org/2.1/queries/
def query_by_id(id):
	result = Event.query.filter(Event.id==id).first()
	if result:
		return result
	else:
		return None
