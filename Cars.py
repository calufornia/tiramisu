import requests
import sys
from flask import Flask


def car_slice():
    r = requests.get(
        "https://api.sandbox.amadeus.com/v1.2/cars/search-airport?location=NCE&pick_up=2016-11-07&drop_off=2016-11-08&lang=EN&currency=USD&provider=ZI&rate_class=ALL&rate_plan=DAILY&rate_filter=ESTIMATED&apikey=NEeYQKLjtZyWXlcUBor348kuPY5C3N8K")
    car_data = r.json()
    cars = car_data['results'][3]
    car_objects = {}
    min_car = Car(cars[0]['vehicle_info'], cars[0]['rates'][0], cars[0]['images'], cars[0]['estimated_total'])


class Car:
    def __init__(self, vehicle_info, rate, images, estimated_total):
        self.vehicle_info = vehicle_info
        self.rate = rate
        self.images = images
        self.estimated_total = estimated_total