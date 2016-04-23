from flask import Blueprint, render_template
from app.models import *

# http://flask-sqlalchemy.pocoo.org/2.1/queries/
def query_by_event_name(look_for):
	result = Event.query.filter(Event.title.ilike(look_for)).all()
	return result
