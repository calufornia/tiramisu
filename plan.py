from flights import *


class Plan:
    def __init__(self, flight, hotels, cars):
        assert isinstance(flight, Flight)
        assert isinstance(hotels, list)
        assert isinstance(cars, list)

        self.flight = flight
        self.hotels = hotels
        self.cars = cars