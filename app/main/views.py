from . import main
from flask import render_template, g
from .. import db
import cloudant
# from flask_cloudant import FlaskCloudant
import yaml

from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from pygments import highlight

syntax = get_lexer_by_name('yaml')


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
    doc_fmt = yaml.dump(doc, default_flow_style=False)
    doc_fmt = highlight(doc_fmt, syntax, HtmlFormatter())
    if len(doc) == 0:
        raise Exception
        # return render_template('404.html'), 404
    return render_template('element.html', doc=doc, doc_fmt=doc_fmt)
