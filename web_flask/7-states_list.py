#!/usr/bin/python3
''' List of states '''
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    ''' Close session '''
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states():
    ''' Render html with all states '''
    states = storage.all(State)
    states = states.values()
    return render_template(
        '7-states_list.html',
        states_list=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
