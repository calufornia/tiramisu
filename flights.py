from hotels import *
from cars import *


def flight_slice(**kwargs):

    basename = "https://api.sandbox.amadeus.com/v1.2/flights/inspiration-search?"

    flights = get_json(basename, **kwargs)
    flight_objects = []
    num_results = 5

    for flight in flights:
        flight_objects += Flight(flight['departure_date'], flight['price'], flight['destination'], flight['airline'], flight['return_date'])
        if len(flight_objects >= num_results):
            break

    return flight_objects


class Flight:
    def __init__(self, departure_date, price, destination, airline, return_date):
        self.departure_date = departure_date
        self.price = price
        self.destination = destination
        self.airline = airline
        self.return_date = return_date

    def __str__(self):
        return 'Destination: ' + self.destination \
             + '<br/>Departure Date: ' + self.departure_date \
             + '<br/>Return Date: ' + self.return_date \
             + '<br/>Airline: ' + self.airline \
             + '<br/>Price: ' + self.price
