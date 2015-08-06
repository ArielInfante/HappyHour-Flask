from app import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSON

class Hour_Agreed(db.Model):
    __tablename__ = "hours_agreed"

    agreed_id = db.Column(db.integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.users_id'))

class Hour_Disagreed(db.Model):
    __tablename__ = "hours_disagreed"

    disagreed_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.users_id'))

class Restaurant_Hour(db.Model):
    __tablename__ = "restaurants_hours"

    yelp_id = db.Column(db.Integer, db.ForeignKey('restaurants.yelp_id'), primary_key=True)
    hour_id = db.Column(db.DateTime, primary_key=True)
    agreed = db.Column(db.Integer, db.ForeignKey('hours_agreed.agreed_id'))
    disagreed = db.Column(db.Integer, db.ForeignKey('hours_disagreed.disagreed_id'))


class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    yelp_id = db.Column(db.String(120), primary_key=True)
    happy_hour = db.Column(db.DateTime, db.ForeignKey('restaurants_hours.hour_id'))
    created_by = db.Column(db.Integer, db.ForeignKey('users.users_id'))

    def __init__(self, yelp_id):
        self.yelp_id = yelp_id
