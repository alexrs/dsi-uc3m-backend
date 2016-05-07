# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from datetime import datetime
from app.models import *
from app import db
import requests
import json
import ast

db.create_all()
tree = ET.parse('cine.xml')
root = tree.getroot()

url_first= "http://www.omdbapi.com/?"
url_second = "&plot=short&r=json&apikey=7afd82c8"

def search_by_id(imdb_id):

    url = url_first+"i="+imdb_id+url_second
    #print(url)

    r = requests.get(url).text
    r = ast.literal_eval(json.loads(json.dumps(r)))
    if r["Response"] == "True":
        return OMDB(r["imdbID"], r["Response"], r["Title"], r["Year"],
                    r["Rated"], r["Released"], r["Runtime"], r["Genre"],
                    r["Director"], r["Writer"], r["Actors"], r["Plot"],
                    r["Language"], r["Country"], r["Awards"],
                    r["Poster"], r["Metascore"], r["imdbRating"], r["imdbVotes"]
                    , r["Type"])

    return OMDB("", "", "", "", "", "", "", "",
                "", "", "", "", "", "", "", "",
                 "", "", "", "")

def search_by_name(title):
    title = unicode(title)

    #print(title)

    if title == u"Los cuentos de Hoffman - ópera PREG. MET CAN":
        title = "Los cuentos de Hoffman"

    if title == u"La viuda alegre - Ópera PREG. MET CAN (Digital)":
        title = "La viuda alegre"

    if title == u"Los maestros cantores de Núremberg - Ópera PREG CAN (Digital)":
        title = u"Los maestros cantores de Núremberg"

    if title == u"El barbero de Sevilla - ópera PREG. MET CAN (Digital)":
        title = "El barbero de Sevilla"

    if title == u"Carmen - ópera PREG. MET CAN (Digital)":
        title = "Carmen"

    if title == u"La dama del lago - Ópera PREG. MET CAN":
        title = "La dama del lago"

    if title == u"Maratón: Los juegos del hambre: Sinsajo parte 1 y parte 2 (Dig)" or title == u"Maratón: Los juegos del hambre: Sinsajo parte 1 y parte 2 (Dig) V.O.S.E.":
        title = "Sinsajo"



    index = title.find("/")
    if (index != -1):
        title = title[:index]

    index = title.find("-")
    if index != -1:
        title = title[index+1:]

    title = title.replace("El Holandes Errante", "El Buque Fantasma")
    title = title.replace("El gran dictador", "The Great Dictator")
    title = title.replace("Tosca de Puccini", "Tosca")
    title = title.replace("CAVALLERIA RUSTICANA, PIETRO MASCAGNI", "CAVALLERIA RUSTICANA")

    for cat in [u"(Ópera Directo)","(Ballet Directo)","(Ballet)"]:
        title = title.replace(cat, "")

    for aut in ["(Giuseppe Verdi)","(Wolfgang Amadeus Mozart)","(Giaccomo Puccini)","(Gaetano Donizzetti)"]:
        title = title.replace(aut, "")

    title = title.replace("(Digital)", "")
    title = title.replace("VERDI", "")
    title = title.replace(u"(Ópera)", "")
    title = title.replace(u"Ópera", "")
    title = title.replace(u"ópera", "")
    title = title.replace("PREG CAN", "")
    title = title.replace(u"/ Sección Oficial SEFF\'15", "")


    title = title.replace("(Zarzuela)","")
    title = title.replace("V.O.S.E.", "")
    title = title.replace("V.O.S.", "")
    title = title.replace("(Dig)", "")
    title = title.replace("(Directo)", "")
    title = title.replace(u"(emisión directo)", "")
    title = title.replace(u"(emisión diferido)", "")
    title = title.replace(u"(Concierto diferido)", "")



    title = title.replace(u"(Milán)", "")
    title = title.replace("Opera en Directo", "")




    title = title.replace("Met LIVE 15-16", "")


    # title = title.replace("(", "")
    # title = title.replace(")", "")

    title = title.replace(u"SEFF´15", "")
    title = title.replace("SEFF'15", "")


    title = title.replace(":", "")
    title = title.replace(".", "")
    title = title.replace(",", "")
    title = title.replace("BALLET", "")

    title = title.replace("LIVE", "")

    title = title.replace("/ Special Screening", "")
    title = title.replace("en Directo", "")
    title = title.replace("PREG MET CAN", "")
    title = title.replace("Met", "")



    title = "+".join(title.split())
    url = url_first+"t="+title+url_second
    #print(url)
    r = requests.get(url).text
    r = ast.literal_eval(json.loads(json.dumps(r)))

    if (r["Response"] == "True"):
        return OMDB(r["imdbID"], r["Response"], r["Title"], r["Year"],
                    r["Rated"], r["Released"], r["Runtime"], r["Genre"],
                    r["Director"], r["Writer"], r["Actors"], r["Plot"],
                    r["Language"], r["Country"], r["Awards"],
                    r["Poster"], r["Metascore"], r["imdbRating"],
                    r["imdbVotes"], r["Type"])

    return OMDB("", "", "", "", "", "", "", "",
                "", "", "", "", "", "", "", "",
                 "", "", "", "")

class OMDB():
    def __init__(self, imdb_id, response, title, year, rated, released, runtime, genre,
                director, writer, actors, plot, language, country, awards, poster,
                 metascore, imdbRating, imdbVotes, type):
        self.imdb_id = imdb_id
        self.response = response
        self.title = title
        self.year = year
        self.rated = rated
        self.released = released
        self.runtime = runtime
        self.genre = genre
        self.director = director
        self.writer = writer
        self.actors = actors
        self.plot = plot
        self.language = language
        self.country = country
        self.awards = awards
        self.poster = poster
        self.metascore = metascore
        self.imdbRating = imdbRating
        self.imdbVotes = imdbVotes
        self.type = type

    def __str__(self):

        return ("imdb_id = "+ self.imdb_id+
                ", response = "+ self.response+
                ", title = "+ self.title+
                ", year = "+ self.year+
                ", rated = "+ self.rated+
                ", released = "+ self.released+
                ", runtime = "+ self.runtime+
                ", genre = "+ self.genre+
                ", director = "+ self.director+
                ", writer = "+ self.writer+
                ", actors = "+ self.actors+
                ", plot = "+ self.plot+
                ", language = "+ self.language+
                ", country = "+ self.country+
                ", awards = "+ self.awards+
                ", poster = "+ self.poster+
                ", metascore = "+ self.metascore+
                ", imdbRating = "+ self.imdbRating+
                ", type = "+ self.type)

#Theater
# for elem in root[0]:
#
#     id = elem.get('theaterId')
#     name = elem.find('name').text
#     telephone = elem.find('telephone').text
#     longitude = elem.find('longitude').text if elem.find('longitude').text is not None else 0.0
#     latitude = elem.find('latitude').text if elem.find('latitude').text is not None else 0.0
#     street = elem.find('address').find('streetAddress').find('street').text
#     city = elem.find('address').find('city').text
#     state = elem.find('address').find('state').text
#     postalCode = elem.find('address').find('postalCode').text
#     country = elem.find('address').find('country').text
#
#     theater = Theater(id, name, telephone, longitude, latitude, street, city, state, postalCode, country)
#     ###db.session.commit(theater)
#
# #Showtime
# for elem in root[2]:
#     date = elem.get('date')
#     theaterId = elem.get('theaterId')
#     eventId = elem.get('movieId')
#
#     showtime = ShowTime(date, theaterId, eventId)
#     #db.session.add(showtime)
#
#     times = elem.find('times').findall('time')
#
#     for time in times:
#         ticketUrl = time.get('ticketUrl')
#         hour = time.text
#         mtime = Time(ticketUrl, hour, eventId, showtime)
#         #db.session.add(mtime)

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


    omdb_ob = None

    imdb = elem.find('imdb')


    if imdb is None:
        imdb = 0
        omdb_ob = search_by_name(title)

    else:
        imdb = imdb.text
        omdb_ob = search_by_id(imdb)


    if duration is None:
        duration = 90
    format = elem.find('format').text
    originalLanguage = elem.find('originalLanguage').text
    genres = elem.find('genres').findall('genre')
    cast = elem.find('cast').findall('actor')
    trailer = elem.find('trailer')
    if trailer is not None:
        trailer = trailer.text
    event = Event(eventId, title, sinopsis, country, ratings, duration, format, originalLanguage, trailer, 7.80, imdb,
                  omdb_ob.response, unicode(omdb_ob.title, "utf-8"), unicode(omdb_ob.year, "utf-8"),
                  omdb_ob.released, omdb_ob.runtime,
                  unicode(omdb_ob.plot, "utf-8"), omdb_ob.language, omdb_ob.country,
                  omdb_ob.awards, omdb_ob.poster, omdb_ob.metascore,
                  omdb_ob.imdbRating, omdb_ob.imdbVotes, omdb_ob.type)

    for genre in genres:
        db.session.add(Genre(genre.text, eventId))

    for genre in omdb_ob.genre.split(","):
        db.session.add(Genre(genre, eventId))

    for rat in ratings:
        db.session.add(Rating(rat.text, eventId))

    db.session.add(Rating(omdb_ob.rated, eventId))

    for actor in cast:
        name = actor.find('firstName').text
        dicaprio = Actor(name)
        dicaprio.movie_actor.append(event)
        db.session.add(dicaprio)

    for actor_name in omdb_ob.actors.split(","):
        actor = Actor(unicode(actor_name, "utf-8"))
        actor.movie_actor.append(event)
        db.session.add(actor)

    crew = elem.find('crew').findall('member')
    for person in crew:
        member = CrewMember(person.find('firstName').text if person.find('firstName') is not None else "NULL", person.find('role').text if person.find('role') is not None else "NULL")
        db.session.add(member)

    for person in omdb_ob.director.split(","):
        member = CrewMember(unicode(person, "utf-8"), "Director")
        db.session.add(member)

    for person in omdb_ob.writer.split(","):
        member = CrewMember(unicode(person, "utf-8"), "Writer")
        db.session.add(member)

    db.session.add(event)
db.session.commit()
