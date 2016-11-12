import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    r = requests.get("https://api.sandbox.amadeus.com/v1.2/hotels/search-circle?apikey=NEeYQKLjtZyWXlcUBor348kuPY5C3N8K&latitude=36.0857&longitude=-115.1541&radius=50&check_in=2016-11-15&check_out=2016-11-17")
    hotels_data = r.json()
    hotels_options = hotels_data['results']


class Hotel:
    def __init__(self,property_name,line1,city,postal_code,country,total_price_amount,total_price_currency,min_daily_rate_amount,min_daily_rate_currency,amenities_description,awards_provider,awards_rating,images,rooms_booking_code,room_currency,room_start_date,room_end_date,rooms_rates_price,descriptions):
        self.property_name = property_name
        self.line1 = line1
        self.city = city
        self.postal_code = postal_code
        self.country = country
        self.total_price_amount = total_price_amount
        self.total_price_currency = total_price_currency
        self.min_daily_rate_amount = min_daily_rate_amount
        self.min_daily_rate_currency = min_daily_rate_currency
        self.amenities_description = amenities_description
        self.awards_provider = awards_provider
        self.awards_rating = awards_rating
        self.images = images
        self.room_booking_code = rooms_booking_code
        self.room_currency = room_currency
        self.room_start_date = room_start_date
        self.room_end_date = room_end_date
        self.room_rates_price = rooms_rates_price
        self.descriptions = descriptions

if __name__ == '__main__':
  app.run()