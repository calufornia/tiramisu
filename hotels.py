from utils import *


def hotel_slice(**kwargs):

    basename = "https://api.sandbox.amadeus.com/v1.2/cars/search-circle?"

    hotels = get_json(basename, kwargs)

    min_hotel = Hotel(hotels[0]['property_name'], hotels[0]['address'], hotels[0]['total_price'], hotels[0]['min_daily_rate'], hotels[0]['amenities'], hotels[0]['awards'], hotels[0]['images'], hotels[0]['rooms'])
    hotel_objects = {}
    for hotel in hotels:
        key = hotel['property_name']

        temp_hotel = Hotel(hotel['property_name'], hotel['address'], hotel['total_price'], hotel['min_daily_rate'], hotel['amenities'], hotel['awards'], hotel['images'], hotel['rooms'])

        if hotel['property_name'] in hotel_objects.keys():
            hotel_objects[key].append(temp_hotel)
        else:
            hotel_objects[key] = [temp_hotel]
    return min_hotel.__str__()


class Hotel:
    def __init__(self,property_name,address,total_price,min_daily_rate,amenities,awards,images,rooms):
        self.property_name = property_name
        self.address = address
        self.total_price = total_price
        self.min_daily_rate = min_daily_rate
        self.amenities = amenities
        self.awards = awards
        self.images = images
        self.rooms = rooms

    def __str__(self):
        return 'Property Name: ' + self.property_name \
               + '<br/>Address: ' + self.address \
               + '<br/>Total Price: ' + self.total_price \
               + '<br/>Amenities: ' + self.amenities \
               + '<br/>rooms: ' + self.rooms