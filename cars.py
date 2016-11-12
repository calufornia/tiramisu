import requests
import sys
from flask import Flask

def car_slice(**kwargs):
    request_string = "https://api.sandbox.amadeus.com/v1.2/cars/search-airport?"

    for key in kwargs:
        request_string += key + "=" + kwargs[key] + "&"

    request_string += "apikey=NEeYQKLjtZyWXlcUBor348kuPY5C3N8K"
    r = requests.get(request_string)
    car_data = r.json()
    providers = car_data['results']
    car_objects = {}

    for p in providers:
        assert isinstance(p, object)
        for c in p['cars']:
            acriss = c['vehicle_info']['acriss_code']
            temp_car = Car(c['vehicle_info']['transmission'],
                    c['vehicle_info']['fuel'], c['vehicle_info']['air_conditioning'], c['vehicle_info']['category'],
                    c['vehicle_info']['type'], c['rates'], c['images'], c['estimated_total'], p['provider'],
                           p['location'], p['address'])

            if acriss not in car_objects.keys():
                car_objects[acriss] = temp_car
            else:
                car_objects[acriss].append(temp_car)

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