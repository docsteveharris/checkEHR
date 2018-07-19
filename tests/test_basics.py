# - [ ] @TODO: (2018-06-13) @resume @refactor switch to flask pytest layout
# # http://flask.pocoo.org/docs/1.0/testing/
# import pytest
from flask import url_for, g, Flask
import requests
from cloudant import couchdb



def test_foo(app):
    # import pdb; pdb.set_trace()
    pass


def test_pytest_flask_app(app):
    '''Check the pytest-flask extension has generated an app via the fixture
    declared in conftest.py'''
    assert isinstance(app, Flask)


def test_app_is_testing(app):
    assert app.config['TESTING'] is True


def test_index_returns_html_and_app_name(app):
    # - [ ] @TODO: (2018-07-19) @fixme work out better way of getting db into g
    # g.db = db  # forces db into request context
    res = app.test_client().get(url_for('main.index'))
    assert res.status_code == 200
    res = res.get_data(as_text=True)
    assert '<html>' in res
    assert '</html>' in res
    # check title corresponds to app
    assert 'checkEHR' in res


def test_couchdb_is_running(app):
    couch_url = app.config['COUCH_URL']
    res = requests.get(couch_url)
    assert res.status_code == 200
    res_json = res.json()
    assert 'couchdb' in res_json.keys()
    assert res_json['version'], '2.1.1'


def test_login_to_couchdb_needs_credentials(app):
    # No credentials
    couch_url = app.config['COUCH_URL']
    res = requests.put(couch_url + '/testing_db_via_requests')
    assert res.status_code == 401


def test_login_to_couchdb_with_credentials(app, couch_url):
    res = requests.get(couch_url)
    assert res.status_code == 200

    # proof of principle that credentials allow PUT
    # try to delete the database
    try:
        res = requests.delete(couch_url + '/testing_db_via_requests')
        res.raise_for_status()
    except requests.exceptions.HTTPError:
        res = requests.put(couch_url + '/testing_db_via_requests')
        assert res.status_code == 201
    finally:
        requests.delete(couch_url + '/testing_db_via_requests')


def test_cloudant_api_works(app):
    '''Try connection with cloudant API rather than requests'''
    with couchdb(app.config['COUCH_USER'],
                 app.config['COUCH_PWD'],
                 url=app.config['COUCH_URL']
                 ) as client:
        assert client.all_dbs() is not None
        assert 'testing_db_via_cloudant' not in client.all_dbs()
        db = client.create_database('testing_db_via_cloudant')
        assert db.exists() is True
        client.delete_database('testing_db_via_cloudant')
        assert db.exists() is False


def test_cloudant_testing_db(app):
    assert g.db is not None
    docs = g.db.all_docs(include_docs=True)
    assert 'total_rows' in docs
    rows = docs['rows']
    assert len(rows) > 0
    doc = rows[0]
    assert 'id' in doc.keys()
    assert '_id' in doc['doc'].keys()
    assert '_rev' in doc['doc'].keys()


def test_flask_bootstrap_extension_loads(app):
    res = app.test_client().get('/')
    res_txt = res.get_data(as_text=True)
    assert 'twitter-bootstrap' in res_txt
    assert '.navbar' in res_txt
