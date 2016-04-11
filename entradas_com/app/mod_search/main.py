import xml.etree.ElementTree as ET
tree = ET.parse('cine.xml')
root = tree.getroot()

# for elem in root[0]:
#     print(elem.get('theaterId'))
#     print(root[0][0].find('name').text)
#     print(root[0][0].find('telephone').text)
#     print(root[0][0].find('longitude').text)
#     print(root[0][0].find('latitude').text)
#     print(root[0][0].find('address').find('streetAddress').find('street').text)
#     print(root[0][0].find('address').find('city').text)
#     print(root[0][0].find('address').find('state').text)
#     print(root[0][0].find('address').find('postalCode').text)
#     print(root[0][0].find('address').find('country').text)
#
#     print("\n")

class Theater:

    def __init__(self, id, name, telephone, longitude, latitude, street, city, state, postalCode, country):
        self.id = id
        self.name = name
        self.telephone = telephone
        self.longitude = longitude
        self.latitude = latitude
        self.street = street
        self.city = city
        self.state = state
        self.postalCode = postalCode
        self.country = country

for elem in root[1]:
#     print(elem.get('movieId'))
#     print(elem.find('officialTitle').text)
#
#     sinopsis = elem.find('sinopsis')
#
#     if sinopsis is not None:
#         print(sinopsis.text)
#
#     print(elem.find('country').text)
#
#     ratings = elem.find('ratings').findall('rating')
#
#     for rating in ratings:
#         print(rating.text)
#
#     print(elem.find('runningTime').text)
#     print(elem.find('format').text)
#
#     print(elem.find('originalLanguage').text)
#     print(elem.find('formatCode').text)
#     print(elem.find('subtitles').text)
#     print(elem.find('version').text)
#
#     genres = elem.find('genres').findall('genre')
#
#     for genre in genres:
#         print(genre.text)
#
#     cast = elem.find('cast').findall('actor')
#
#     for actor in cast:
#         print(actor.find('firstName').text)
#
#     crew = elem.find('crew').findall('member')
#
#     for person in crew:
#         print(person.find('role').text)
#         if not person.find('firstName') is None:
#             print(person.find('firstName').text)
#
#     print(elem.find('cartel').text)
#
#     trailer = elem.find('trailer')
#
#     if trailer is not None:
#         print(trailer.text)
# #
#     print("\n")

class Event:

    def __init__(self, id, title, sinopsis, country, ratings, runningTime, format, originalLanguage, formatCode, subtitles, version, genres, cast, crew, cartel, trailer):
        self.id = id
        self.title = title
        self.sinopsis = sinopsis
        self.country = country
        self.ratings = ratings
        self.duration = runningTime
        self.format = format
        self.originalLanguage = originalLanguage
        self.formatCode = formatCode
        self.subtitles = subtitles
        self.version = version
        self.genres = genres
        self.cast = cast #List of Actor
        self.crew = crew #List of CreeMember
        self.cartel = cartel
        self.trailer = trailer
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

# for elem in root[2]:
#     print(elem.get('date'))
#     print(elem.get('theaterId'))
#     print(elem.get('movieId'))
#
#     times = elem.find('times').findall('time')
#
#     for time in times:
#         print(time.get('ticketUrl'))
#         print(time.text)
#
#     print("\n")

class ShowTime:
    def __init__(self, date, theaterId, movieId, time, ticketUrl, time):
        self.date = date
        self.eventId = theaterId
        self.time = time
        self.ticketUrl = ticketUrl
        self.time

class Actor:
    def __init__(self, firstName):
        self.firstName = firstName

class CrewMember:
    def __init__(self, firstName, role):
        self.firstName = firstName
        self.role = role

# <showTime date="20151112" theaterId="2" movieId="30171">
# <times>
#   <time ticketUrl="http://cine.entradas.com/entradas/a001009.do?identidad=710&amp;idcanal=2&amp;idcine=2&amp;idprov=28&amp;idpeli=30171&amp;idSesion=29518&amp;fecha=20151112&amp;idSala=1">2015</time>
# </times>
# </showTime>
