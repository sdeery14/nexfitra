import os

def get_secret(secret_name):
    try:
        with open(f"/run/secrets/{secret_name}") as secret_file:
            return secret_file.read().strip()
    except IOError:
        return os.environ.get(secret_name)

class Config:
    SECRET_KEY = get_secret('flask_secret_key')
    SQLALCHEMY_DATABASE_URI = f"postgresql://flask_user:{get_secret('flask_user_password')}@db:5432/flask_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = get_secret('mail_password')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
    SERVER_NAME = '127.0.0.1:5000'  # Replace with your domain
    APPLICATION_ROOT = '/'
    PREFERRED_URL_SCHEME = 'http'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f"postgresql://flask_test_user:{get_secret('flask_test_user_password')}@db:5432/flask_test_db"
    WTF_CSRF_ENABLED = False  # Disable CSRF protection in testing
    LOGIN_DISABLED = True  # Disable login requirement for testing
    MAIL_SUPPRESS_SEND = True  # Disable sending emails during tests
    MAIL_DEFAULT_SENDER = 'test@test.com'

class ProductionConfig(Config):
    pass

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
