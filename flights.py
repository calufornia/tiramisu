from cars import *
from hotels import *
from plan import *


def flight_slice(uflight_toggle, **kwargs):

    basename = "https://api.sandbox.amadeus.com/v1.2/flights/inspiration-search?"

    flights = get_json(basename, **kwargs)
    flight_objects = []
    num_results = 5
    if uflight_toggle:
        visited_states = set()

    for flight in flights:
        if uflight_toggle and flight['destination'] not in visited_states:
            visited_states.add(flight['destination'])
        elif uflight_toggle and flight['destination'] in visited_states:
            continue

        flight_objects += [Flight(flight['departure_date'], flight['price'], flight['destination'], flight['airline'], flight['return_date'])]
        if len(flight_objects) >= num_results:
            break

    plans = []
    for flight in flight_objects:
        hotel_kwargs = {'location': flight.destination, 'check_in': flight.departure_date, 'check_out': flight.return_date}
        car_kwargs = {'location': flight.destination, 'pick_up': flight.departure_date, 'drop_off': flight.return_date}
        plans += [Plan(flight, hotel_slice(**hotel_kwargs), car_slice(**car_kwargs))]

    return plans


class Flight:
    def __init__(self, departure_date, price, destination, airline, return_date):
        self.departure_date = departure_date
        self.price = price
        self.destination = destination
        self.airline = airline
        self.return_date = return_date

    def __str__(self):
        return 'Destination: ' + self.destination \
             + ' Departure Date: ' + self.departure_date \
             + ' Return Date: ' + self.return_date \
             + ' Airline: ' + self.airline \
             + ' Price: ' + self.price