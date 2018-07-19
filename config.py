'''
Congfiguration settings for the application
'''

# - [ ] TODO  2018-06-09: move usernames, passwords, and keys to a separate
#   file that can remain outside of source control although the structure
#   below means that the SECRET_KEY (for example) is set in the environment
#   and not in the file under version control

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    '''
    Parent config class that shares settings between different possible
    configurations
    '''

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my precious'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    _PROTOCOL = 'http://'
    _COUCH_URL = '127.0.0.1:5984'
    COUCH_URL = _PROTOCOL + _COUCH_URL
    COUCH_DB = 'chkehr-dev'
    COUCH_USER = 'testyMcTestFace'
    COUCH_PWD = 'testyMcTestFace'


class TestingConfig(Config):
    TESTING = True
    _PROTOCOL = 'http://'
    _COUCH_URL = '127.0.0.1:5984'
    COUCH_URL = _PROTOCOL + _COUCH_URL
    COUCH_DB = 'chkehr-test'
    COUCH_USER = 'testyMcTestFace'
    COUCH_PWD = 'testyMcTestFace'


class ProductionConfig(Config):
    DEBUG = False


# key:value dictionary that returns the appropriate config
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
