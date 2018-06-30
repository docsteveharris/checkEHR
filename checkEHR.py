# define the Flask application instance here
import os
from app import create_app
import cloudant
from flask import g

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


def connect_db():
    """Returns a new connection to the CouchDB database."""
    db = app.config['COUCHDB_DATABASE']
    client = cloudant.client.CouchDB(
        app.config['COUCHDB_USER'],
        app.config['COUCHDB_PWD'],
        url=app.config['COUCHDB_SERVER'])
    client.connect()
    # import pdb; pdb.set_trace()
    return client[db]


@app.before_request
def before_request():
    """Make sure we are connected to the database each request."""
    g.db = connect_db()


@app.cli.command()
def test():
    '''Run the unit tests'''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
