# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py
from app import db
from app.mod_auth

# Define a User model
class User(Base):

	__tablename__ = 'auth_user'

	# User Name
	name = db.Column(db.String(128), nullable=False)

	# Identification Data: email & password
	email = db.Column(db.String(128), nullable=False, unique=True)
	password = db.Column(db.String(192), nullable=False)

	# New instance instantiation procedure
	def __init__(self, name, email, password):
	    self.name = name
	    self.email = email
	    self.password = password

	def __repr__(self):
	    return '<User %r>' % (self.name) 
