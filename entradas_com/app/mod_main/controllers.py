# Import flask dependencies
from flask import Blueprint, render_template, redirect
from app.models import *

# Import module forms
from app.mod_main.forms import SearchForm

mod_main = Blueprint('main', __name__,)

# Set the route and accepted methods
@mod_main.route('/')
def index():
	return render_template("main/index.html")


def get_suggestions():
	pass

