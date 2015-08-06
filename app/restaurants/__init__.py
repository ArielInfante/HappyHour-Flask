from flask import Blueprint

restaurant = Blueprint('restaurant', __name__)

from . import views
