from datetime import datetime
from app import db

class Base(db.Model):
	__abstract__ = True
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

# Define a User model
class User(Base):

    # User Name
    username = db.Column(db.String(128), nullable=False)

    # Identification Data: email & password
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(192), nullable=False)

    # New instance instantiation procedure
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.username)


class Theater(Base):
    theaterId = db.Column(db.Integer, unique=True)
    name  = db.Column(db.String(30), unique=False)
    telephone = db.Column(db.String(12), unique=False)
    longitude = db.Column(db.Float, unique=False)
    latitude = db.Column(db.Float, unique=False)
    street = db.Column(db.String(50), unique=False)
    city = db.Column(db.String(20), unique=False)
    state = db.Column(db.String(20), unique=False)
    postalCode = db.Column(db.Integer, unique=False)
    country = db.Column(db.String(12), unique=False)

    def __init__(self, theaterId, name, telephone, longitude, latitude, street, city, state, postalCode, country):
        self.theaterId = int(theaterId)
        self.name = name
        self.telephone = telephone
        self.longitude = float(longitude)
        self.latitude = float(latitude)
        self.street = street
        self.city = city
        self.state = state
        self.postalCode = int(postalCode)
        self.country = country

class ShowTime(Base):

    date = db.Column(db.Date)
    theaterId = db.Column(db.Integer)
    movieId = db.Column(db.Integer)

    def __init__(self, date, theaterId, movieId):
        self.date = datetime.strptime(date, '%Y%m%d')
        self.theaterId = int(theaterId)
        self.movieId = int(movieId)

class Time(Base):

    ticketUrl = db.Column(db.String(100))
    hour = db.Column(db.String(15)) #TODO: Parse (check?)
    movieId = db.Column(db.Integer)
    showtime_id = db.Column(db.Integer, db.ForeignKey('show_time.id'))
    showtime_time = db.relationship('ShowTime', backref=db.backref('times', lazy='dynamic'))


    def __init__(self, ticketUrl, hour, movieId, showtime):
        self.ticketUrl = ticketUrl
        self.hour = hour
        self.movieId = int(movieId)
        self.showtime = showtime


class CrewMember(Base):

    firstName = db.Column(db.UnicodeText(100))
    role = db.Column(db.String(50))

    def __init__(self, firstName, role):
        self.firstName = firstName
        self.role = role


movie_actor = db.Table('movie_actor', db.Column("event_id", db.Integer, db.ForeignKey('event.id')), db.Column("actor_id", db.Integer, db.ForeignKey('actor.id')))

class Actor(Base):

    firstName = db.Column(db.UnicodeText(100))
    movie_actor = db.relationship('Event', secondary=movie_actor, backref = db.backref('actors', lazy='dynamic'))

    def __init__(self, firstName):
        self.firstName = firstName

class Genre(Base):

    name = db.Column(db.String(25))
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    event_genre = db.relationship('Event', backref=db.backref('genres', lazy='dynamic'))

    def __init__(self, name, event):
		self.name = name
		self.event_id = int(event)

class Rating(Base):
    rating = db.Column(db.String(60))

    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    event_rating = db.relationship('Event', backref=db.backref('Rating', lazy='dynamic'))

    def __init__(self, rating, event):
        self.rating = rating
        self.event_id = int(event)



#Propongo hacer una tabla evento-teatro, para tener la relacion n-m
class Event(Base):
    eventId = db.Column(db.Integer)
    title = db.Column(db.UnicodeText(200))
    sinopsis = db.Column(db.UnicodeText(600))
    country = db.Column(db.String(20))
    duration = db.Column(db.Integer)
    format = db.Column(db.String(10))
    originalLanguage = db.Column(db.String(30))
    trailer = db.Column(db.String(15))
    price = db.Column(db.Float)
    imdb = db.Column(db.String(20))

    omdb_response = db.Column(db.String(5))
    omdb_title = db.Column(db.UnicodeText(200))
    omdb_year = db.Column(db.UnicodeText(10))
    omdb_released = db.Column(db.String(25))
    omdb_runtime = db.Column(db.Integer)
    omdb_plot = db.Column(db.UnicodeText(600))
    omdb_language = db.Column(db.String(25))
    omdb_country = db.Column(db.String(25))
    omdb_awards = db.Column(db.String(100))
    omdb_poster = db.Column(db.String(100))
    omdb_metascore = db.Column(db.Integer)
    omdb_imdbRating = db.Column(db.Integer)
    omdb_imdbVotes = db.Column(db.Integer)
    omdb_type = db.Column(db.String(50))



    def __init__(self, eventId, title, sinopsis, country, ratings, runningTime, format, originalLanguage, trailer, price, imdb,
                omdb_response, omdb_title, omdb_year, omdb_released, omdb_runtime, omdb_plot,
                omdb_language, omdb_country,omdb_awards, omdb_poster, omdb_metascore, omdb_imdbRating,
                omdb_imdbVotes, omdb_type):
        self.eventId = int(eventId)
        self.title = title
        self.sinopsis = sinopsis
        self.country = country
        self.ratings = ratings # list
        self.duration = int(runningTime)
        self.format = format
        self.originalLanguage = originalLanguage
        self.trailer = trailer
        self.price = price
        self.imdb = imdb

        self.omdb_response = omdb_response
        self.omdb_title = omdb_title
        self.omdb_year = omdb_year
        self.omdb_released = omdb_released
        self.omdb_runtime = omdb_runtime
        self.omdb_plot = omdb_plot
        self.omdb_language = omdb_language
        self.omdb_country = omdb_country
        self.omdb_awards = omdb_awards
        self.omdb_poster = omdb_poster
        self.omdb_metascore = omdb_metascore
        self.omdb_imdbRating = omdb_imdbRating
        self.omdb_imdbVotes = omdb_imdbVotes
        self.omdb_type = omdb_type
