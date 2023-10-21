#!/usr/bin/python3
"""
script that starts a Flask web application
Including another route to return a diffeerent page
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Funtion return Hello HBNB!"""
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Function return HBNB"""
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """Function that accepts Argument"""
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
