# Import flask dependencies
from flask import Blueprint, render_template

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_main = Blueprint('index', __name__)

# Set the route and accepted methods
@mod_main.route('/')
def index():
    return render_template("main/index.html")