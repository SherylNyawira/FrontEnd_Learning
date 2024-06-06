#!/usr/bin/python3

"""
a flask script
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/hbnb_filters")
def hbnb_filters():
    """ this is the hbnb filters folder """
    states = storage.all(State)
    states = dict(sorted(states.items(), key=lambda item: item[1].name))
    cities = storage.all(City)
    cities = dict(sorted(cities.items(), key=lambda item: item[1].name))
    amenities = storage.all(Amenity)
    amenities = dict(sorted(amenities.items(), key=lambda item: item[1].name))
    return render_template("10-hbnb_filters.html", states=states, cities=cities, amenities=amenities)

@app.teardown_appcontext
def teardown(error):
    """ this is the teardown for the database called  data"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
