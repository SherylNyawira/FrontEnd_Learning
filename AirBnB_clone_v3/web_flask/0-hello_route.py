#!/usr/bin/python3

"""
a script that starts a flask web application
"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    """ this is the homepage """
    return "Hello HBNB!"


if __name__ == "__main__":
    """ this is the unimportable script """
    app.run(host="0.0.0.0", port="5000")
