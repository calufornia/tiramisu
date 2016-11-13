from utils import *


def car_slice(**kwargs):

    basename = "https://api.sandbox.amadeus.com/v1.2/cars/search-airport?"

    providers = get_json(basename, **kwargs)
    car_objects = {}
    n = 5

    min_provider_info = providers[0]
    min_car_info = min_provider_info['cars'][0]
    min_car = Car(min_car_info['vehicle_info']['transmission'],
                    min_car_info['vehicle_info']['fuel'], min_car_info['vehicle_info']['category'],
                    min_car_info['vehicle_info']['type'], min_car_info['rates'], min_car_info['estimated_total'], min_provider_info['provider'],
                           min_provider_info['address'])

    i = 0
    for provider in providers:
        if i == n:
            break

        for car in provider['cars']:
            if i == n:
                break

            acriss = car['vehicle_info']['acriss_code']
            temp_car = Car(car['vehicle_info']['transmission'],
                    car['vehicle_info']['fuel'], car['vehicle_info']['category'],
                    car['vehicle_info']['type'], car['rates'], car['estimated_total'], provider['provider'],
                    provider['address'])

            if acriss in car_objects.keys():
                car_objects[acriss].append(temp_car)
                i += 1

            else:
                car_objects[acriss] = [temp_car]
                i += 1
    return car_objects.__str__()

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
        address_full = ""
        for key in self.address.keys():
            address_full += self.address[key] + ", "

        provider_full = ""
        for key in self.provider.keys():
            provider_full += '<br/>' + key + ': ' + self.provider[key]

        rates_full = ""
        for rate in self.rates:
            rates_full +=   'Type: ' + rate['type'] + ', '
            rates_full +=   'Price: ' + rate['price']['amount'] + ' ' + rate['price']['currency']

        return '<br/>Provider: ' + provider_full \
            + '<br/>Address: ' + address_full\
            + '<br/>Transmission: ' + self.transmission\
            + '<br/>Fuel: ' + self.fuel\
            + '<br/>Category: ' + self.category\
            + '<br/>Type: ' + self.type\
            + '<br/>Rates: ' + rates_full\
            + '<br/>Estimated_total:\t' + self.estimated_total['amount'] + " " + self.estimated_total['currency']
