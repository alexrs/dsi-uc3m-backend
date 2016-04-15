import xml.etree.ElementTree as ET
tree = ET.parse('cine.xml')
root = tree.getroot()
import config

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

class Base(db.Model):
	__abstract__ = True
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class Theater(Base):
    __tablename__ = 'theater'

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
    __tablename__ = 'showtime'

    date = db.Column(db.String(40)) #TODO: PARSE THIS AS A DATE
    theaterId = db.Column(db.Integer)
    movieId = db.Column(db.Integer)

    def __init__(self, date, theaterId, movieId):
        self.date = date
        self.theaterId = int(theaterId)
        self.movieId = int(movieId)

class Time(Base):
    __tablename__ = "time"

    ticketUrl = db.Column(db.String(100))
    hour = db.Column(db.String(5)) #TODO: Parse
    movieId = db.Column(db.Integer)

    def __init__(self, ticketUrl, hour, movieId):
        self.ticketUrl = ticketUrl
        self.hour = hour
        self.movieId = int(movieId)

class Actor(Base):
    __tablename__ = 'actor'
    firstName = db.Column(db.String(100))

    def __init__(self, firstName):
        self.firstName = firstName

class CrewMember(Base):
    __tablename__ = 'crew_member'
    firstName = db.Column(db.String(100))
    role = db.Column(db.String(50))

    def __init__(self, firstName, role):
        self.firstName = firstName
        self.role = role

class Event(Base):
    __tablename__ = 'event'
    movieId = db.Column(db.Integer)
    title = db.Column(db.String(50))
    sinopsis = db.Column(db.Text)
    country = db.Column(db.String(20))
    # ratings is a list.
    duration = db.Column(db.Integer)
    format = db.Column(db.String(10))
    originalLanguage = db.Column(db.String(30))
    #genres
    #cast
    #crew
    trailer = db.Column(db.String(15))



    def __init__(self, movieId, title, sinopsis, country, ratings, runningTime, format, originalLanguage, genres, cast, crew, trailer):
        self.movieId = int(movieId)
        self.title = title
        self.sinopsis = sinopsis
        self.country = country
        self.ratings = ratings # list
        self.duration = int(runningTime)
        self.format = format
        self.originalLanguage = originalLanguage
        self.genres = genres #list
        self.cast = cast #List of Actor
        self.crew = crew #List of CreeMember
        self.trailer = trailer


db.create_all()

"""Theater"""
for elem in root[0]:

    id = elem.get('theaterId')
    name = root[0][0].find('name').text
    telephone = root[0][0].find('telephone').text
    longitude = root[0][0].find('longitude').text
    latitude = root[0][0].find('latitude').text
    street = root[0][0].find('address').find('streetAddress').find('street').text
    city = root[0][0].find('address').find('city').text
    state = root[0][0].find('address').find('state').text
    postalCode = root[0][0].find('address').find('postalCode').text
    country = root[0][0].find('address').find('country').text

    theater = Theater(id, name, telephone, longitude, latitude, street, city, state, postalCode, country)
    db.session.add(theater)

db.session.commit()


"""Showtime"""
for elem in root[2]:
    date = elem.get('date')
    theaterId = elem.get('theaterId')
    movieId = elem.get('movieId')

    showtime = ShowTime(date, theaterId, movieId)
    db.session.add(showtime)

    times = elem.find('times').findall('time')

    for time in times:
        ticketUrl = time.get('ticketUrl')
        hour = time.text
        mtime = Time(ticketUrl, hour, movieId)
        db.session.add(mtime)

db.session.commit()

"""Event"""
for elem in root[1]:
    movieId = elem.get('movieId')
    title = elem.find('officialTitle').text
    sinopsis = elem.find('sinopsis')
    country = elem.find('country').text
    ratings = elem.find('ratings').findall('rating')
    duration = elem.find('runningTime').text
    if duration is None:
        duration = 90
    format = elem.find('format').text
    originalLanguage = elem.find('originalLanguage').text
    genres = elem.find('genres').findall('genre')
    cast = elem.find('cast').findall('actor')
    crew = elem.find('crew').findall('member')
    trailer = elem.find('trailer')

    event = Event(movieId, title, sinopsis, country, ratings, duration, format, originalLanguage, genres, cast, crew, trailer)
    db.session.add(event)
db.session.commit()

 
# <movie movieId="18507">
    # <officialTitle>&#211;pera La Flauta M&#225;gica</officialTitle>
    # <sinopsis>Proyecci&#243;n de la &#243;pera -La flauta m&#225;gica- de Mozart.</sinopsis>
    # <runningTime>90</runningTime>
    # <format>35 mm.</format>
    # <country>ESPA&#209;A</country>
    # <ratings>
        # <rating>PENDIENTE DE CALIFICACI&#211;N</rating>
    # </ratings>
    # <originalLanguage>Castellano</originalLanguage>
    # <formatCode>0</formatCode>
    # <subtitles>0</subtitles>
    # <version>S</version>
    # <genres>
        # <genre>Opera</genre>
    # </genres>
    # <cast></cast>
    # <crew>
        # <member>
            # <role>Director</role>
            # <firstName>Mozart</firstName>
        # </member>
    # </crew>
    # <cartel>opera.gif</cartel>
# </movie>



# <showTime date="20151112" theaterId="2" movieId="30171">
# <times>
#   <time ticketUrl="http://cine.entradas.com/entradas/a001009.do?identidad=710&amp;idcanal=2&amp;idcine=2&amp;idprov=28&amp;idpeli=30171&amp;idSesion=29518&amp;fecha=20151112&amp;idSala=1">2015</time>
# </times>
# </showTime>
