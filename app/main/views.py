from . import main
from flask import render_template, g
from .. import db
import cloudant
# from flask_cloudant import FlaskCloudant


@main.route('/')
def index():
    all_docs = db.all_docs(include_docs=True)
    # attach docs to g context so available without passing as separate
    # argument
    g.docs = all_docs['rows']
    return render_template('index.html')


@main.route('/element/<id>')
def element(id):
    result = cloudant.result.Result(db.all_docs, include_docs=True)
    doc = result[id]
    if len(doc) == 0:
        return render_template('404.html'), 404
    return render_template('element.html', doc=doc)
