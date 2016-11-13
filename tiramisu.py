from flask import Flask, request
from flask_wtf import Form
from wtforms import StringField, BooleanField
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
    unique = BooleanField('Unique',validators=[DataRequired()])



app = Flask(__name__)
app.secret_key="YOLOSWAG"


@app.route('/',methods=['GET', 'POST'])
def index():
    form = APIRequestForm()

    if request.method=='POST':

        kwargs = {'origin': form.origin._value(), 'departure_date': form.departure.data.strftime('%Y-%m-%d'), 'return_date': form.arrival.data.strftime('%Y-%m-%d')}
        results = flight_slice(False, **kwargs)
        if len(results)==0:
            return render_template("results.html")
        elif len(results)==1:
            return render_template("results.html",plan1=results[0])
        elif len(results)==2:
            return render_template("results.html",plan1=results[0],plan2=results[1])
        elif len(results)==3:
            return render_template("results.html",plan1=results[0],plan2=results[1],plan3=results[2])
        elif len(results)==4:
            return render_template("results.html",plan1=results[0],plan2=results[1],plan3=results[2],plan4=results[3])
        else:
            return render_template("results.html",plan1=results[0],plan2=results[1],plan3=results[2],plan4=results[3],plan5=results[4])
    else:
        return render_template("index.html",form=form)


if __name__=='__main__':
    app.run()