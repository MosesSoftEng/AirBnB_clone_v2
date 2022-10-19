# :book: 0x04. AirBnB clone - Web framework
## Flask
Flask is a lightweight Web Server Gateway Interface (WSGI) web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.

### Web Server Gateway Interface (WSGI)
Is a simple calling convention for web servers to forward requests to web applications or frameworks written in the Python programming language. 

### Project setup
```bash
# Create web_flask package
mkdir web_flask
touch web_flask/README.md web_flask/__init__.py
chmod +x __init__.py

# install pep8 v1.7
sudo pip install pep8==1.7.0

# Install flask
sudo pip3 install Flask


# Run flask web app for file in package web_flask
python3 -m web_flask.<module name>
```

# :computer: Tasks
## [0. Hello Flask!](0-hello_route.py), [__init__.py]( )
Script to start Flask web application on 0.0.0.0:5000 with route / strict_slashes=False and displaying "Hello HBNB!" 

```bash
touch web_flask/0-hello_route.py
chmod +x web_flask/0-hello_route.py

pep8 web_flask/0-hello_route.py

# Start flask server file
python3 -m web_flask.0-hello_route
```

## [1. HBNB ](1-hbnb_route.py), [__init__.py]( )
Script to start Flask web application on 0.0.0.0:5000 with route / strict_slashes=False and displaying "Hello HBNB!" 

```bash
touch web_flask/1-hbnb_route.py
chmod +x web_flask/1-hbnb_route.py

pep8 web_flask/1-hbnb_route.py

# Start flask server file
python3 -m web_flask.1-hbnb_route
```

# :books: References
1. [Web Server Gateway Interface](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface)
2. [W3C validator for Holberton School](https://github.com/holbertonschool/W3C-Validator)

# :man: Author and Credits.
This project was done by [SE. Moses Mwangi](https://github.com/MosesSoftEng). Feel free to get intouch with me;

:iphone: WhtasApp [+254115227963](https://wa.me/254115227963)

:email: Email [moses.soft.eng@gmail.com](mailto:moses.soft.eng@gmail.com)

:thumbsup: A lot of thanks to [ALX-Africa Software Engineering](https://www.alxafrica.com/) program for the project requirements.