#!/usr/bin/python3
"""Script that displays and the render the sstates"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def display_states():
    states = sorted(storage.all('State').values(), key=lambda i: i.name)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def close_strorage(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
