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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
