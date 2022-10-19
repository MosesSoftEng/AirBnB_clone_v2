#!/usr/bin/python3
"""Run Flask web application on socket 0.0.0.0:5000

With route / strict_slashes=False and displaying "Hello HBNB!"
"""
from flask import Flask

# Create an instance of this Flask class passing the name of this module
#   for location of other web files; templates.
app = Flask(__name__)

# Disable 404 status code on Accessing the URL with a trailing slash gloablly
app.url_map.strict_slashes = False


# Routes
@app.route('/')
def hello_HBNB():
    """Display 'Hello HBNB!'"""
    return 'Hello HBNB!'

# Set socket to run the app on
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
