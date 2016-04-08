# Import flask dependencies
from flask import Blueprint, render_template, request

# Define the blueprint: 'auth', set its url prefix: app.url/
mod_search = Blueprint('search', __name__)

# Set the route and accepted methods
@mod_search.route('/search')
def search():
	query = request.args.get('query')
	category = request.args.get('category')
	return render_template("search/results.html")