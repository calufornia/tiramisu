# tiramisu
Tiramisu is a travel app that allows users to plan spontaneous trips. It utilizes various API's of Amadeus's Travel Innovation Sandbox, specifically the Flight Inspiration Search, Hotel Airport Search, and Car Rental Airport Search APIs. Given an origin location and a range of dates, the website will output the five cheapest flights from that start location, and a list of five hotels and rental cars that operate in the destination location.

To run the app:
1. Set up a Python virtual environment by first running pip install virtualenv, and then virtualenv -p /usr/bin/python2.7 venv
2. Enter the virtual environment by execeuting source venv/bin/activate, and run pip install -r requirements.txt
3. To launch the app, cd into tiramisu and run python tiramisu.py
