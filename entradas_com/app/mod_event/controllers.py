# Import flask dependencies
from flask import Blueprint, render_template, redirect, request
from app.models import *
from app import db

mod_event = Blueprint('event', __name__,)

# Set the route and accepted methods
@mod_event.route('/event/<id>')
def event(id):
	#return id
	return render_template("event/event.html")