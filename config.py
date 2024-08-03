import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DB_NAME = os.environ.get('DB_NAME')
    DB_USER = os.environ.get('DB_USER')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = os.environ.get('DB_PORT', '5432')  # Default to 5432 for PostgreSQL
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
    SERVER_NAME = '127.0.0.1:5000'  # Replace with your domain
    APPLICATION_ROOT = '/'
    PREFERRED_URL_SCHEME = 'http'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    DB_NAME_TEST = os.environ.get('DB_NAME_TEST')
    DB_USER_TEST = os.environ.get('DB_USER_TEST')
    DB_PASSWORD_TEST = os.environ.get('DB_PASSWORD_TEST')
    DB_HOST_TEST = os.environ.get('DB_HOST_TEST')
    DB_PORT_TEST = os.environ.get('DB_PORT_TEST', '5432')  # Default to 5432 for PostgreSQL
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER_TEST}:{DB_PASSWORD_TEST}@{DB_HOST_TEST}:{DB_PORT_TEST}/{DB_NAME_TEST}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False  # Disable CSRF protection in testing
    LOGIN_DISABLED = True  # Disable login requirement for testing
    MAIL_SUPPRESS_SEND = True  # Disable sending emails during tests

class ProductionConfig(Config):
    pass

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
