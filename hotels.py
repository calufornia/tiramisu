from utils import *


def hotel_slice(**kwargs):

    basename = "https://api.sandbox.amadeus.com/v1.2/hotels/search-airport?"

    hotels = get_json(basename, **kwargs)
    num_results = 5

    hotel_objects = []
    for hotel in hotels:

        hotel_objects += [Hotel(hotel['property_name'], hotel['address'], hotel['total_price'], hotel['min_daily_rate'], hotel['amenities'], hotel['awards'], hotel['images'], hotel['rooms'])]
        if len(hotel_objects) >= num_results:
            break

    return hotel_objects


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
        room_descriptions = ""
        for room in self.rooms:
            room_descriptions += room['booking_code'] + ": "
        for description in room['descriptions']:
            room_descriptions += description + ", "
        room_descriptions += " "

        hotel_amenities = ""
        for amenity in self.amenities:
            hotel_amenities += amenity['description'] + ", "

        address_full = ""
        for key in self.address.keys():
            address_full += self.address[key] + ", "

        awards_all = ""
        for award in self.awards:
            awards_all += award['rating'] + " by " + award['provider']

        return 'Property Name: ' + self.property_name \
           + ' Address: ' + address_full \
           + ' Total Price: ' + self.total_price['currency'] + " " + self.total_price['amount'] \
           + ' ' + room_descriptions \
           + ' Amenities: ' + hotel_amenities \
           + ' Awards: ' + awards_all


