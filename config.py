import sqlalchemy as sql

db_config = {
    'username': 'root',
    'password':'PASSWORD',
    'host': '127.0.0.1',
    'port': 3306,
    'database': 'fantasy2'
    }

db_string = sql.engine.url.URL(drivername = 'mysql', **db_config)

class Config:
    SECRET_KEY = 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_DATABASE_URI = db_string
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    @staticmethod
    def init_app(app):
            pass


class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
    }
