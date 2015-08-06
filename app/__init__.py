from flask import Flask
# from users.models import AnonymousUser
from flask.ext.sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.moment import Moment
from flask.ext.bcrypt import Bcrypt
from flask_wtf import CsrfProtect
from flask.ext.login import LoginManager

'''
    EXTENSIONS
'''
toolbar = DebugToolbarExtension()
moment = Moment()
bcrypt = Bcrypt()
csrf = CsrfProtect()
login_manager = LoginManager()
db = SQLAlchemy()

'''
    START APP
'''
app = Flask(__name__)


'''
    CONFIGURE APP
'''
from config import config
app.config.from_object(config['development'])
# app.config.from_object(settings.DevConfig)
# config['development'].init_app(app)


'''
    ROUTES
'''
from mains import main
app.register_blueprint(main)

from users import user
app.register_blueprint(user)

from restaurants import restaurant
app.register_blueprint(restaurant)

# from auths import auth
# app.register_blueprint(auth)


'''
    LOGIN MANAGER
'''
# login_manager.login_view = ''
# login_manager.login_message = ''
# login_manager.login_message_category = ''
from users.models import AnonymousUser
login_manager.anonymous_user = AnonymousUser
login_manager.session_protection = 'basic'  # Choose ' "basic" ' or ' "strong" ' or "None"

'''
    PYJADE
'''
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

'''
    INITIALIZE EXTENSIONS
'''
db.init_app(app)
toolbar.init_app(app)
moment.init_app(app)
bcrypt.init_app(app)
csrf.init_app(app)
login_manager.init_app(app)

# with app.app_context():
#     db.create_all()