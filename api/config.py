import os
import redis
from os import environ as env

class Config(object):

    
    # This database connection is for local development
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:''@localhost/keywords_test'
    SQLALCHEMY_DATABASE_URI = env.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('FLASK_KEY')

    SESSION_TYPE ='redis'
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    SESSION_REDIS = redis.from_url("redis://redis:6379")
    # SESSION_REDIS = redis.from_url("redis://default:redispw@localhost:49153")