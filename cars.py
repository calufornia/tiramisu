from utils import *


def car_slice(**kwargs):

    basename = "https://api.sandbox.amadeus.com/v1.2/cars/search-airport?"

    providers = get_json(basename, **kwargs)
    car_objects = {}

    min_provider_info = providers[0]
    min_car_info = min_provider_info['cars'][0]
    min_car = Car(min_car_info['vehicle_info']['transmission'],
                    min_car_info['vehicle_info']['fuel'], min_car_info['vehicle_info']['air_conditioning'], min_car_info['vehicle_info']['category'],
                    min_car_info['vehicle_info']['type'], min_car_info['rates'], min_car_info['estimated_total'], min_provider_info['provider'],
                           min_provider_info['address'])

    for provider in providers:
        for car in provider['cars']:
            acriss = car['vehicle_info']['acriss_code']
            temp_car = Car(car['vehicle_info']['transmission'],
                    car['vehicle_info']['fuel'], car['vehicle_info']['air_conditioning'], car['vehicle_info']['category'],
                    car['vehicle_info']['type'], car['rates'], car['estimated_total'], provider['provider'],
                           provider['address'])

            if acriss in car_objects.keys():
                car_objects[acriss].append(temp_car)

            else:
                car_objects[acriss] = [temp_car]
    return min_car.__str__()


class Car:
    def __init__(self, transmission, fuel, category, type, rates, estimated_total, provider, address):
        self.transmission = transmission
        self.fuel = fuel
        self.category = category
        self.type = type
        self.rates = rates
        self.estimated_total = estimated_total
        self.provider = provider
        self.address = address

    def __str__(self):
        return 'Transmission: ' + self.transmission\
            + '<br/>Fuel: ' + self.fuel\
            + '<br/>Category: ' + self.category\
            + '<br/>Type: ' + self.type\
            + '<br/>Rates: ' + self.rates\
            + '<br/>Estimated_total: ' + self.estimated_total\
            + '<br/>Provider: ' + self.provider\
            + '<br/>Address: ' + self.address
        
