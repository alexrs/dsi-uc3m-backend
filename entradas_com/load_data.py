import xml.etree.ElementTree as ET
from datetime import datetime
from app.models import *
from app import db

db.create_all()
tree = ET.parse('cine.xml')
root = tree.getroot()
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
    event = Event(eventId, title, sinopsis, country, ratings, duration, format, originalLanguage, trailer, 7.80)

    for genre in genres:
        db.session.add(Genre(genre.text, eventId))
    for rat in ratings:
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
