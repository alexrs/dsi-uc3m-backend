# Import flask dependencies
from flask import Blueprint, render_template, redirect, request
from app.models import *
from app import db

mod_detail = Blueprint('details', __name__,)

# Set the route and accepted methods
@mod_detail.route('/detail/<id>')
def index(id):
	return id