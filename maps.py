import googlemaps
from datetime import datetime

class Maps():

    def __init__(self):
        pass

    def makeMap(self):
        self.key = 'AIzaSyAT0EqXyaTRo081KIXI8WleI1kivOFJkg0'
        self.address = ''
        self.lat = '-2.519495'
        self.long = '-44.247695'
        self.city = 'São Luis, Maranhão'
        self.dir_origin = "Sao Francisco, São Luis - Maranhão"
        self.dir_destiny = "Monte Castelo, São Luis - Maranhão"
        self.placetype = 'bar'
        gmaps = googlemaps.Client(key=self.key)
        geocode_result = gmaps.geocode(self.city)
        reverse_geocode_result = gmaps.reverse_geocode((self.lat,self.long))
        now = datetime.now()
        directions_result = gmaps.directions(self.dir_origin,
                                            self.dir_destiny,
                                            mode="transit",
                                            departure_time=now)
        gplaces = gmaps.places(query=self.placetype,
                            location={'lat':self.lat,'lng':self.long})
        
