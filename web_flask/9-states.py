#!/usr/bin/python3
"""Script that displays and the render the sstates"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def display_states():
    states = sorted(storage.all('State').values(), key=lambda i: i.name)
    return render_template("9-states.html", states=states, value='all')


@app.route("/states/<id>", strict_slashes=False)
def display_states_by_id(id):
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', states=state, value='id')
    return render_template('9-states.html', states=state, value='none')


@app.teardown_appcontext
def close_strorage(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
