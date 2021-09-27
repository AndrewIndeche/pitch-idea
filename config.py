import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.urandom(32)
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://andrew:123456@localhost/pitch'

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

class DevelopmentConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options={
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
    }
