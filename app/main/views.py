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


