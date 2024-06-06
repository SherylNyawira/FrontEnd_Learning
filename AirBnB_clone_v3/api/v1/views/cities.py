#!/usr/bin/python3

""" creates a new view for state objects
handles all default RESTFul api actions
"""
from flask import abort, request, jsonify
from api.v1.views import app_views
from models.state import State
from models.city import City
from models import storage


@app_views.route('/cities')
@app_views.route('/cities/<city_id>', methods=['GET', 'DELETE', 'PUT'])
def route_cities(city_id=None):
    """ displays all states in the database """
    if request.method == 'GET':
        if not city_id:
            abort(404)
        city = storage.get(City, city_id)
        if not city:
            abort(404)
        return jsonify(city.to_dict())
    elif request.method == 'DELETE':
        if not city_id:
            abort(404)
        city = storage.get(City, city_id)
        storage.delete(city)
        storage.save()
        return jsonify({}), 200
    elif request.method == 'POST':
        # creating a new instance
        try:
            newcity = request.get_json()
        except Exception:
            abort(400, description="Not a JSON")

        if newcity.get('name') is None:
            abort(400, description="Missing name")
        else:
            newcity = City(**newcity)
            newcity.save()
            storage.reload()
            return jsonify(newcity.to_dict()), 201
    elif request.method == 'PUT':
        if not city_id:
            abort(404)
        city = storage.get(City, city_id)
        if not city:
            abort(404)
        try:
            data = request.get_json()
        except Exception:
            abort(400, description="Not a JSON")

        # checking for exceptions of updates
        if data.get('id'):
            del(data['id'])
        if data.get('created_at'):
            del(data['created_at'])
        if data.get('updated_at'):
            del(data['updated_at'])
        # end for exceptions of updates

        for key, value in data.items():
            setattr(city, key, value)
        storage.save()
        storage.reload()
        return jsonify(city.to_dict()), 200


@app_views.route('/states/<state_id>/cities', methods=['GET', 'POST'])
def route_all_cities(state_id=None):
    """ routes for all cities in a state"""
    states = storage.all(State)
    key = "State.{}".format(state_id)

    if request.method == 'GET':
        if states.get(key):
            cities = []
            stateCities = states[key].cities
            for stateCity in stateCities:
                cities.append(stateCity.to_dict())
            return jsonify(cities), 200
        else:
            abort(404)
    elif request.method == 'POST':
        # creating a new instance
        if not states.get(key):
            abort(404)

        try:
            newcity = request.get_json()
        except Exception:
            return "Not a JSON", 400

        if newcity.get('name') is None:
            abort(400, description="Missing name")
        else:
            newcity = City(**newcity)
            setattr(newcity, 'state_id', state_id)
            newcity.save()
            storage.reload()
            return jsonify(newcity.to_dict()), 201
