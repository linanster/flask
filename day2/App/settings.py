import os

import redis as redis

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Config():
    SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"
    # flask-session-3
    # SESSION_TYPE = 'redis'
    # SESSION_REDIS = redis.Redis(host='10.30.30.101',port='6379')

class DevelopConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///sqlite-develop.db"

class TestConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///sqlite-test.db"

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///sqlite-production.db"


envs = {
    "development" : DevelopConfig,
    "test" : TestConfig,
    "production" : ProductionConfig,
    "default" : DevelopConfig
}