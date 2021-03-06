'''
    GLOBAL SETTINGS:
'''
from secret import *
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = APP_SECRET_KEY
    ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
    UPLOAD_IMG_FOLDER = os.path.abspath(os.path.join(os.getcwd(), 'app', 'static', 'uploads'))
    ALLOWED_IMG_EXTENSIONS = ['png', 'jpg', 'jpeg']
    '''
    EXTENSIONS = [
                    'ext.db',
                    'ext.assets',
                    'ext.login_manager',
                    'ext.gravatar',
                    'ext.toolbar',
                ]
    '''

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    DEBUG_TB_PROFILER_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    # WTF_CSRF_ENABLED = False

    '''
    DATABASE CONNECTION
    '''
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE

class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False

    '''
    DATABASE CONNECTION
    '''
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE

class ProductionConfig(BaseConfig):
    WTF_CSRF_ENABLED = True
    '''
    DATABASE CONNECTION
    '''
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE

config = {
    'development': DevelopmentConfig,
    'test': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}