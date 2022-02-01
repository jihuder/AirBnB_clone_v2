#!/usr/bin/python3
''' Cities by states '''
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    ''' Close session '''
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states_cities():
    ''' Render a list of cities gruop by states '''
    states = storage.all(State)
    return render_template(
        '8-cities_by_states.html',
        states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
