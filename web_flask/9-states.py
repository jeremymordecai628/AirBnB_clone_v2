#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """Display a HTML page with the list of all State objects"""
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_cities(id):
    """Display a HTML page with the list of City objects linked to a State"""
    state = storage.get(State, id)
    if state is None:
        return render_template('9-not_found.html')
    else:
        cities = sorted(state.cities, key=lambda x: x.name)
        return render_template('9-states_cities.html', state=state, cities=cities)


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
