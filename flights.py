import requests
import sys
from flask import Flask

app = Flask(__name__)


@app.route('/origin/<origin>/departure_date/<departure_date>') # YYYY-MM-DD--YYYY-MM-DD
def hello_world(origin, departure_date):
    r = requests.get("http://api.sandbox.amadeus.com/v1.2/flights/inspiration-search?origin={origin}&departure_date={departure_date}&duration=7--9&max_price=500&apikey=NEeYQKLjtZyWXlcUBor348kuPY5C3N8K".format(origin=origin, departure_date=departure_date))
    flight_data = r.json()
    flights = flight_data['results']
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