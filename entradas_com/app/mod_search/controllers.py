from flask import Blueprint, render_template, request
from app.models import *

mod_search = Blueprint('search', __name__,)


@mod_search.route('/search/', methods=['POST'])
def search():
	print query_by_event_name(str(request.form['query']))
	return str(request.form['query'])
	
# http://flask-sqlalchemy.pocoo.org/2.1/queries/
def query_by_event_name(look_for):
	#result = Event.query.filter(Event.title.ilike(look_for)).all()
	result = Event.query.order_by(Event.title).all()
	return result
