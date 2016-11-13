
import requests

from flask import Flask


app = Flask(__name__)

@app.route('/')
def airports():
    r = requests.get("https://api.sandbox.amadeus.com/v1.2/location/SFO?apikey=NEeYQKLjtZyWXlcUBor348kuPY5C3N8K")
    city_info = r.json()
    nearby_airports_objects = city_info['airports']
    nearby_airports = []
    for airport in nearby_airports_objects:
        nearby_airports.append(airport['code'])
    return nearby_airports

if __name__ == '__main__':
    app.run()