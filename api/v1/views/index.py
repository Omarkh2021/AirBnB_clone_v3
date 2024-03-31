#!/usr/bin/python3
"""Initialize flask functions"""
from flask import jsonify, make_response
from api.v1.views import app_views
from models import storage

classes = {"amenities": 47, 
  "cities": 36, 
  "places": 154, 
  "reviews": 718, 
  "states": 27, 
  "users": 31}


@app_views.route('/status', strict_slashes=False)
def view_status():
    """Returns a JSON"""
    response = jsonify({"status": "OK"})
    response.headers["Content-Type"] = "application/json"
    return response


@app_views.route('/stats', strict_slashes=False)
def storage_stats():
    """Returns a JSON"""
    dict = {}
    for cls, name in classes.items():
        dict.update({name: storage.count(cls)})
    response = jsonify(dict)
    response.headers["Content-Type"] = "application/json"
    return response
