# Import flask and template operators
from flask import Flask, render_template
# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_main.controllers import mod_main as main_module
from app.mod_search.controllers import mod_search as search_module


# Register blueprint(s)
app.register_blueprint(main_module)
app.register_blueprint(search_module)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()