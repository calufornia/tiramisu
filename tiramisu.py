import requests
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    r = requests.get("http://api.sandbox.amadeus.com/v1.2/flights/inspiration-search?origin=BOS&departure_date=2016-11-16--2016-11-26&duration=7--9&max_price=500&apikey=NEeYQKLjtZyWXlcUBor348kuPY5C3N8K")
    return r.text


if __name__ == '__main__':
    app.run()
