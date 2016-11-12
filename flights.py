from utils import *


def flight_slice(**kwargs):

    basename = "https://api.sandbox.amadeus.com/v1.2/cars/inspiration-search?"

    flights = get_json(basename, kwargs)
    flight_objects = {}
    min_flight = Flight(flights[0]['departure_date'], flights[0]['price'], flights[0]['destination'], flights[0]['airline'], flights[0]['return_date'])

    for flight in flights:
        value = flight['destination']
        temp_flight = Flight(flight['departure_date'], flight['price'], flight['destination'], flight['airline'], flight['return_date'])

        if flight['destination'] in flight_objects.keys():
            flight_objects[value].append(temp_flight)
        else:
            flight_objects[value] = [temp_flight]
    return min_flight.__str__()


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
