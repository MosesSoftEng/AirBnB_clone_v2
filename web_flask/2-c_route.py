#!/usr/bin/python3
"""Script to start Flask web application

Requirements:
    - Web application must be listening on 0.0.0.0, port 5000
    - Routes use option strict_slashes=False in thier definitions

Routes:
    /           display 'hello HBNB'
    /HBNB       display 'HBNB'
    /c/<text>   display 'C <text>'
"""
from flask import Flask

# Create an instance of this Flask class passing the name of this module
#   for location of other web files; templates.
app = Flask(__name__)

# Disable 404 status code on Accessing the URL with a trailing slash gloablly
# app.url_map.strict_slashes = False


# Routes definitions
@app.route('/', strict_slashes=False)
def show_hello_HBNB():
    """Display 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def show_HBNB():
    """Display 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_C(text):
    """Display 'c <text>'"""
    return 'C {}'.format(text.replace('_', ' '))

# Set socket to run the app on
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
