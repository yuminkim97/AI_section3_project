import os
basedir = os.path.abspath(os.path.dirname(__file__))

'''
export FLASK_APP=musical_app
export DATABASE_URI='postgres://mdlklips:3RV4qozF-rLqMXISM9TCGldcNCKySSBN@john.db.elephantsql.com:5432/mdlklips'
export FLASK_ENV=development
'''

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    # SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URI']

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

# class StagingConfig(Config):
#     DEVELOPMENT = True
#     DEBUG = True

# class TestingConfig(Config):
#     TESTING = True