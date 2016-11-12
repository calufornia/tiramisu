import requests
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    r = requests.get("http://api.sandbox.amadeus.com/v1.2/flights/inspiration-search?origin=BOS&departure_date=2016-11-16--2016-11-26&duration=7--9&max_price=500&apikey=NEeYQKLjtZyWXlcUBor348kuPY5C3N8K")
    flight_data = r.json()
    flights = flight_data['results']
    flight_objects = {}
    for flight in flights:
        if flights['destination'] in flight_objects.keys():
            flight_objects[flights['destination']].append(flight(flights['departure_date'], flights['price'], flights['destination'], flights['airline'], flights['return_date']))
        else:
            flight_objects[flights['destination']] = [flight(flights['departure_date'], flights['price'], flights['destination'], flights['airline'], flights['return_date'])]
    return r.text

class Flight:
  def __init__(self, departure_date, price, destination, airline, return_date):
       self.departure_date = departure_date
       self.price = price
       self.destination = destination
       self.airline = airline
       self.return_date = return_date


if __name__ == '__main__':
    app.run()
