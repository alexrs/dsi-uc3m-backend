from flask import Blueprint, render_template, request
from app.models import *

mod_search = Blueprint('search', __name__,)


@mod_search.route('/search/', methods=['POST'])
def search():
	query = str(request.form['query'])
	events = query_by_event_name(query)
	return render_template("search/search-results.html", query=query, events=events)
	
# http://flask-sqlalchemy.pocoo.org/2.1/queries/
def query_by_event_name(look_for):
	result = Event.query.filter(Event.title.like(look_for + "%")).all()
	#result = Event.query.order_by(Event.title).all()
	return result
