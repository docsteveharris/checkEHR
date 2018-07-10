from . import main
from flask import render_template, g
from .. import db
# from flask_cloudant import FlaskCloudant


@main.route('/')
def index():
    all_docs = db.all_docs(include_docs=True)
    # attach docs to g context so available without passing as separate
    # argument
    g.docs = all_docs['rows']
    return render_template('index.html')


@main.route('/testthis')
def testthis():
    # proof that the database set up is working and db is available
    # - [ ] @TODO: (2018-07-07) convert this to a unit test
    doc = db.get('0b2f89159bd3602d6448d6ca2b000f68')
    return doc.content()['_rev']
    # return 'testing 123'
