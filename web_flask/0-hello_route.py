#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask

# Create an instance of this Flask class passing the name of this module
#   for location of other web files; templates.
app = Flask(__name__)

# Routes
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"

# Set socket to run the app on only if accessed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
