#!/usr/bin/python3
'''Flask web Framework'''
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''Return Hello HBNB'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def name():
    '''Return Name'''
    return 'HBNB'


@app.route('/c/<txt>', strict_slashes=False)
def display_c_text(txt):
    """Function that returns text variable"""
    return 'C {}'.format(txt.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<txt>', strict_slashes=False)
def python_route(txt='is cool'):
    """Returns text variable"""
    return 'Python {}'.format(txt.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """ /number/<n> route return """
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n=None):
    """ /number_template/<n> route return """
    if isinstance(n, int):
        return render_template("5-number.html", n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
