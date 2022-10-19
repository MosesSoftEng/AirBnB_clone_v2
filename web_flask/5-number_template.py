#!/usr/bin/python3
"""Script to start Flask web application

Requirements:
    - Web application must be listening on 0.0.0.0, port 5000
    - Routes use option strict_slashes=False in thier definitions

Routes:
    /
        Display 'hello HBNB'
    /HBNB
        Display 'HBNB'
    /c/<text>
        Display 'C <text>'
        Replacing _ with space in <text>
    /python/(<text>)
        Display 'Python <text>', <text> default value 'is cool'
        Replacing _ with space in <text>
    /number/<n>
        display “n is a number” only if n is an integer
    /number_template/<n>
        Display a HTML page only if n is an integer
        H1 tag: 'Number: n' inside the tag BODY
"""
from flask import Flask
from flask import render_template

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
    """Display 'c <text>'
    Replacing _ with space in <text>
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_Python(text='is cool'):
    """Display 'Python <text>'
    Replacing _ with space in <text>
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    """Display 'n is a number' only if n is an integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def show_number_template(n):
    """Display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


# Set socket to run the app on
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
