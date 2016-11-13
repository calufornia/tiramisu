
import requests

from flask import Flask


app = Flask(__name__)

@app.route('/')
def airports():
    r = requests.get("https://api.sandbox.amadeus.com/v1.2/location/SFO?apikey=NEeYQKLjtZyWXlcUBor348kuPY5C3N8K")
    city_info = r.json()
    airports = city_info['airports']
    airport_options
    for airport in airports
        airport_options.append(airport['code'])






if __name__ == '__main__':
    app.run()