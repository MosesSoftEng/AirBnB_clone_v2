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
## [0. Hello Flask!](0-hello_route.py), [__init__.py](__init__.py)
Script to start Flask web application on 0.0.0.0:5000 with route / strict_slashes=False and displaying "Hello HBNB!" 

```bash
touch web_flask/0-hello_route.py
chmod +x web_flask/0-hello_route.py

pep8 web_flask/0-hello_route.py

# Start flask server file
python3 -m web_flask.0-hello_route

# Test endpoint
curl 0.0.0.0:5000 ; echo "" | cat -e
```

## [1. HBNB ](1-hbnb_route.py)
Script to start Flask web application on 0.0.0.0:5000 with route / strict_slashes=False and displaying "Hello HBNB!" and /hbnb: display “HBNB”

```bash
touch web_flask/1-hbnb_route.py
chmod +x web_flask/1-hbnb_route.py

pep8 web_flask/1-hbnb_route.py

# Start flask server file
python3 -m web_flask.1-hbnb_route

# Test endpoint
curl 0.0.0.0:5000/hbnb ; echo "" | cat -e
```

## [2. C is fun!](2-c_route.py)
Script to start Flask web application on 0.0.0.0:5000 with route / strict_slashes=False and displaying "Hello HBNB!" and /hbnb: display "HBNB" and /c/<text> display "C<text>" replacing _ in <text> with space

```bash
touch web_flask/2-c_route.py
chmod +x web_flask/2-c_route.py

pep8 web_flask/2-c_route.py

# Start flask server file
python3 -m web_flask.2-c_route
```

### Test
```bash
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/is_fun ; echo "" | cat -e
C is fun$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/cool ; echo "" | cat -e
C cool$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ 
```

## [3. C is fun!](2-c_route.py)
Script to start Flask web application

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
        Replace _ with space in <text>
    /python/(<text>)
        Display 'Python <text>', <text> default value 'is cool'
        Replace _ with space in <text>

```bash
touch web_flask/3-python_route.py
chmod +x web_flask/3-python_route.py

pep8 web_flask/3-python_route.py

# Start flask server file
python3 -m web_flask.3-python_route
```

### Tests
```
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/is_magic ; echo "" | cat -e
Python is magic$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python ; echo "" | cat -e
Python is cool$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/ ; echo "" | cat -e
Python is cool$
guillaume@ubuntu:~$ 
```

## [4. Is it a number?](4-number_route.py)
Script to start Flask web application

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
        Replace _ with space in <text>
    /python/(<text>)
        Display 'Python <text>', <text> default value 'is cool'
        Replace _ with space in <text>
    /number/<n>
        display “n is a number” only if n is an integer

```bash
touch web_flask/4-number_route.py
chmod +x web_flask/4-number_route.py

pep8 web_flask/4-number_route.py

# Start flask server file
python3 -m web_flask.4-number_route
```

### Tests
```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/89 ; echo "" | cat -e
89 is a number$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/8.9 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ 
```

## [5. Number template](5-number_template.py)
Script to start Flask web application

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
        Replace _ with space in <text>
    /python/(<text>)
        Display 'Python <text>', <text> default value 'is cool'
        Replace _ with space in <text>
    /number/<n>
        Display 'n is a number' only if n is an integer
    /number_template/<n> 
        Display a HTML page only if n is an integer
        H1 tag: 'Number: n' inside the tag BODY

```bash
touch web_flask/5-number_template.py
chmod +x web_flask/5-number_template.py
mkdir -p web_flask/templates
touch web_flask/templates/5-number.html

pep8 web_flask/5-number_template.py

# Start flask server file
python3 -m web_flask.5-number_template
```

### Tests
```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/89 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 89</H1>
    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/8.9 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/python 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ 
```

# :books: References
1. [Web Server Gateway Interface](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface)
2. [W3C validator for Holberton School](https://github.com/holbertonschool/W3C-Validator)

# :man: Author and Credits.
This project was done by [SE. Moses Mwangi](https://github.com/MosesSoftEng). Feel free to get intouch with me;

:iphone: WhtasApp [+254115227963](https://wa.me/254115227963)

:email: Email [moses.soft.eng@gmail.com](mailto:moses.soft.eng@gmail.com)

:thumbsup: A lot of thanks to [ALX-Africa Software Engineering](https://www.alxafrica.com/) program for the project requirements.