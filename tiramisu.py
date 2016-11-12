import requests
import sys
from flask import Flask, request
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
from flask import render_template
from flights import *
from flask_wtf.csrf import CsrfProtect

class APIRequestForm(Form):
    SECRET_KEY= "YOLOSWAG"
    origin = StringField('Origin',validators = [DataRequired()])
    departure = DateField('Departure',validators=[DataRequired()],format='%Y-%m-%d')
    arrival = DateField('Arrival',validators=[DataRequired()],format='%Y-%m-%d')


app = Flask(__name__)
app.secret_key="YOLOSWAG"


@app.route('/',methods=['GET', 'POST'])
def index():
    form = APIRequestForm()

    if request.method=='POST':
        kwargs = {}
        kwargs['origin'] = form.origin._value()
        kwargs['departure_date'] = form.departure.data.strftime('%Y-%m-%d')
        kwargs['return_date'] = form.arrival.data.strftime('%Y-%m-%d')
        print("Origin is", form.origin)
        print("Departure is", form.departure)
        print("Arrival is", form.arrival)
        #call to query
        return str("Search results:")+ "<br/>" + flight_slice(**kwargs)
    else:
        return render_template("index.html",form=form)


if __name__=='__main__':
    app.run()