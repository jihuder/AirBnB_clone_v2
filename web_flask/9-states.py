#!/usr/bin/python3
''' State and states '''
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    ''' Close session '''
    storage.close()


@app.route('/states/', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state_or_states(id=None):
    ''' list states '''
    states = storage.all(State)

    if not id:
        states = states.values()
        return render_template('7-states_list.html',
                               states_list=states)

    state = 'State.{}'.format(id)
    if state in states:
        return render_template('9-states.html',
                               title='State: {}'.format(states[state].name),
                               states_list=states[state])

    return render_template('9-states.html',
                           states_list=None)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
