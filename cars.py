from utils import *


def car_slice(**kwargs):

    basename = "https://api.sandbox.amadeus.com/v1.2/cars/search-airport?"

    providers = get_json(basename, **kwargs)
    car_objects = []
    num_results = 5

    i = 0
    for provider in providers:
        if i == num_results:
            break

        for car in provider['cars']:
            if i == num_results:
                break

            car_objects += [Car(car['vehicle_info']['acriss_code'], car['vehicle_info']['transmission'],
                    car['vehicle_info']['fuel'], car['vehicle_info']['category'],
                    car['vehicle_info']['type'], car['rates'], car['estimated_total'], provider['provider'],
                    provider['address'])]

            i += 1
            
    return car_objects


class Car:
    def __init__(self, acriss, transmission, fuel, category, type, rates, estimated_total, provider, address):
        self.acriss = acriss
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
            provider_full += key + ': ' + self.provider[key]

        rates_full = ""
        for rate in self.rates:
            rates_full +=   'Type: ' + rate['type'] + ', '
            rates_full +=   'Price: ' + rate['price']['amount'] + ' ' + rate['price']['currency']

        # return ' Provider: ' + provider_full \
        #     + ' Address: ' + address_full\
        #     + ' Acriss: ' + self.acriss\
        #     + ' Transmission: ' + self.transmission\
        #     + ' Fuel: ' + self.fuel\
        #     + ' Category: ' + self.category\
        #     + ' Type: ' + self.type\
        #     + ' Rates: ' + rates_full\
        #     + ' Estimated_total:\t' + self.estimated_total['amount'] + " " + self.estimated_total['currency']

        return 'Address: ' + address_full + ', ' \
               + ' Transmission: ' + self.transmission + ', ' \
               + ' Category: ' + self.category + ', ' \
               + ' Type: ' + self.type + ', ' \
               + ' Rates: ' + rates_full + ', ' \
               + ' Estimated_total:\t' + self.estimated_total['amount'] + " " + self.estimated_total['currency']