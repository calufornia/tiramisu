from utils import *


def car_slice(**kwargs):

    basename = "https://api.sandbox.amadeus.com/v1.2/cars/search-airport?"

    providers = get_json(basename, kwargs)
    car_objects = {}

    for provider in providers:
        for car in provider['cars']:
            acriss = car['vehicle_info']['acriss_code']
            temp_car = Car(car['vehicle_info']['transmission'],
                    car['vehicle_info']['fuel'], car['vehicle_info']['air_conditioning'], car['vehicle_info']['category'],
                    car['vehicle_info']['type'], car['rates'], car['images'], car['estimated_total'], provider['provider'],
                           provider['location'], provider['address'])

            if acriss in car_objects.keys():
                car_objects[acriss].append(temp_car)

            else:
                car_objects[acriss] = temp_car

    return car_objects


class Car:
    def __init__(self, transmission, fuel, air_conditioning, category, type, rates, images, estimated_total, provider,
                 location, address):
        self.transmission = transmission
        self.fuel = fuel
        self.air_conditioning = air_conditioning
        self.category = category
        self.type = type
        self.rates = rates
        self.images = images
        self.estimated_total = estimated_total
        self.provider = provider
        self.location = location
        self.address = address
