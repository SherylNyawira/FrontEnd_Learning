#!/usr/bin/python3

""" creates a new view for state objects
handles all default RESTFul api actions
"""
from flask import abort, request, jsonify
from api.v1.views import app_views
from models.state import State
from models import storage


@app_views.route('/states/', methods=['GET'])
@app_views.route('/states')
def route_states():
    """ displays all states in the database """
    states = storage.all(State)
    stateList = []

    for stateId in states:
        obj = states[stateId].to_dict()
        stateList.append(obj)

    return jsonify(stateList)


methods = ['GET', 'POST', 'PUT', 'DELETE']


@app_views.route('/states/', methods=methods[1:])
@app_views.route('/states/<state_id>', methods=methods)
def route_states_id(state_id=None):
    """ routes for all states """
    states = storage.all(State)

    if state_id:
        key = "State.{}".format(state_id)

    if request.method == 'GET':
        if states.get(key):
            state = states[key].to_dict()
            return jsonify(state), 200
        else:
            abort(404)
    elif request.method == 'POST':
        # creating a new instance
        try:
            newState = request.get_json()
        except Exception:
            abort(400, description="Not a JSON")

        if newState.get('name') is None:
            abort(400, description="Missing name")
        else:
            newState = State(**newState)
            newState.save()
            storage.reload()
            return jsonify(newState.to_dict()), 201
    elif request.method == 'DELETE':
        if not states.get(key):
            abort(404)
        else:
            storage.delete(states[key])
            storage.save()
            return jsonify({}), 200
    elif request.method == 'PUT':
        if not states.get(key):
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
        state = states.get(key)
        for key, value in data.items():
            setattr(state, key, value)
        storage.save()
        storage.reload()
        return jsonify(state.to_dict()), 200
