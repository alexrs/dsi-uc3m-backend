import xml.etree.ElementTree as ET
tree = ET.parse('cine.xml')
root = tree.getroot()
import config

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

class Base(db.Model):
	__abstract__ = True
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

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
    #hour = db.Column(db.Date)
    movieId = db.Column(db.Integer)

    showtime_id = db.Column(db.Integer, db.ForeignKey('show_time.id'))

    showtime_time = db.relationship('ShowTime', backref=db.backref('times', lazy='dynamic'))


    def __init__(self, ticketUrl, hour, movieId, showtime):
        self.ticketUrl = ticketUrl
        self.hour = hour
        #self.hour =  datetime.datetime.strptime(hour, '%Y%m%d')
        self.movieId = int(movieId)
        self.showtime = showtime


class CrewMember(Base):
    firstName = db.Column(db.String(100))
    role = db.Column(db.String(50))

    def __init__(self, firstName, role):
        self.firstName = firstName
        self.role = role


movie_actor = db.Table('movie_actor', db.Column("event_id", db.Integer, db.ForeignKey('event.id')), db.Column("actor_id", db.Integer, db.ForeignKey('actor.id')))

class Actor(Base):
    firstName = db.Column(db.String(100))

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
    title = db.Column(db.String(200))
    sinopsis = db.Column(db.Text)
    country = db.Column(db.String(20))
    #ratings
    duration = db.Column(db.Integer)
    format = db.Column(db.String(10))
    originalLanguage = db.Column(db.String(30))
    #genres
    #cast
    #crew


    trailer = db.Column(db.String(15))

    def __init__(self, eventId, title, sinopsis, country, ratings, runningTime, format, originalLanguage, genres, trailer):
        self.eventId = int(eventId)
        self.title = title
        self.sinopsis = sinopsis
        self.country = country
        self.ratings = ratings # list
        self.duration = int(runningTime)
        self.format = format
        self.originalLanguage = originalLanguage
        #self.genres = genres #list --> en realidad no lo es
        self.trailer = trailer


db.create_all()

#Theater
for elem in root[0]:

    id = elem.get('theaterId')
    name = elem.find('name').text
    telephone = elem.find('telephone').text
    longitude = elem.find('longitude').text if elem.find('longitude').text is not None else 0.0
    latitude = elem.find('latitude').text if elem.find('latitude').text is not None else 0.0
    street = elem.find('address').find('streetAddress').find('street').text
    city = elem.find('address').find('city').text
    state = elem.find('address').find('state').text
    postalCode = elem.find('address').find('postalCode').text
    country = elem.find('address').find('country').text

    theater = Theater(id, name, telephone, longitude, latitude, street, city, state, postalCode, country)
    db.session.add(theater)

#Showtime
for elem in root[2]:
    date = elem.get('date')
    theaterId = elem.get('theaterId')
    eventId = elem.get('movieId')

    showtime = ShowTime(date, theaterId, eventId)
    db.session.add(showtime)

    times = elem.find('times').findall('time')

    for time in times:
        ticketUrl = time.get('ticketUrl')
        hour = time.text
        mtime = Time(ticketUrl, hour, eventId, showtime)
        db.session.add(mtime)

#Event
for elem in root[1]:
    eventId = elem.get('movieId')
    title = elem.find('officialTitle').text
    sinopsis = elem.find('sinopsis')
    if sinopsis is not None:
        sinopsis = sinopsis.text
    country = elem.find('country').text
    ratings = elem.find('ratings').findall('rating')
    duration = elem.find('runningTime').text
    if duration is None:
        duration = 90
    format = elem.find('format').text
    originalLanguage = elem.find('originalLanguage').text
    genres = elem.find('genres').findall('genre')
    cast = elem.find('cast').findall('actor')
    trailer = elem.find('trailer')
    if trailer is not None:
        trailer = trailer.text
    event = Event(eventId, title, sinopsis, country, ratings, duration, format, originalLanguage, genres, trailer)

    for genre in genres:
        db.session.add(Genre(genre.text, eventId))
    for rat in ratings:
        print rat.text
        db.session.add(Rating(rat.text, eventId))

    for actor in cast:
        name = actor.find('firstName').text
        dicaprio = Actor(name)
        dicaprio.movie_actor.append(event)
        db.session.add(dicaprio)


    crew = elem.find('crew').findall('member')
    for person in crew:
		db.session.add(CrewMember(person.find('firstName').text if person.find('firstName') is not None else "NULL", person.find('role').text if person.find('role') is not None else "NULL"))
    db.session.add(event)
db.session.commit()
