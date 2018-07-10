# define the Flask application instance here
import os
from app import create_app, db
# import cloudant
from flask import g

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.before_request
def before_request():
    """Make sure we are connected to the database each request."""
    g.db = db


@app.shell_context_processor
def make_shell_context():
    return dict(db=db)


@app.cli.command()
def test():
    '''Run the unit tests'''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
