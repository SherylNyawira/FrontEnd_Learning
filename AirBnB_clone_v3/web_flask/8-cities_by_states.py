#!/usr/bin/python3

""" a script that starts a flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def route_cities_by_states():
    """ a route to the state """
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)

    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """ closes the database again at the end of the request """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
