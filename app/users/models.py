from app import db, bcrypt, login_manager
from datetime import datetime
import re
from flask import redirect, url_for
from flask.ext.login import UserMixin, AnonymousUserMixin

class Buddies(db.Model, UserMixin):
    __tablename__ = 'buddies'

    followers_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    following_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    buddies_on = db.Column(db.DateTime, default=datetime.utcnow())

class AnonymousUser(AnonymousUserMixin):
    def __init__(self):
        self.username = "Guest"

    # def __repr__(self):
    #     return '<User %r>' % self.username

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    username_check = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(120), unique=True)
    name = db.Column(db.String(120))
    password = db.Column(db.String(70))
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    privacy = db.Column(db.Boolean, default=True)
    avatar = db.Column(db.String(120), default=None)
    thumbnail = db.Column(db.String(120), default=None)
    following = db.relationship('Buddies', foreign_keys=[Buddies.following_id],
                                backref=db.backref('follower', lazy='joined'),
                                lazy='dynamic',
                                cascade='all, delete-orphan')
    followers = db.relationship('Buddies', foreign_keys=[Buddies.followers_id],
                                backref=db.backref('following', lazy='joined'),
                                lazy='dynamic',
                                cascade='all, delete-orphan')

    def __init__(self, username = None, email = None, name = None, password = None):
        self.username = username
        self.username_check = username.lower()
        self.email = email
        self.name = name
        self.password = User.hash_password(password)

    def __repr__(self):
        return '<User %r>' % self.username

    @staticmethod
    def hash_password(password_to_hash):
        return bcrypt.generate_password_hash(password_to_hash)

    def verify_password(self, password_to_verify):
        return bcrypt.check_password_hash(self.password, password_to_verify)

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def check_username_taken(check_username):
        print check_username
        userUsername = User.query.filter_by(username_check=check_username.lower()).first()
        if userUsername is not None:
            return True
        return False

    @staticmethod
    def check_email_taken(check_email):
        print check_email
        userEmail = User.query.filter_by(email=check_email).first()
        print userEmail
        if userEmail is not None:
            return True
        return False

    @staticmethod
    def compare_user_id(main_id, compare_id):
        print main_id
        print compare_id # username to compare to

        main_id = int(main_id.get_id())
        compare_id = int(User.query.filter_by(username_check=compare_id.lower()).first().id)

        print main_id
        print compare_id
        print bool(main_id == compare_id)
        return bool(main_id == compare_id)

    # def is_authenticated(self):
    #     return True
    #
    # def is_active(self):
    #     return True
    #
    # def is_anonymous(self):
    #     return False
    #
    # def get_id(self):
    #     try:
    #         return unicode(self.id)
    #     except NameError:
    #         return str(self.id)




    # def follow(self, user):
    #     if not self.is_following(user):
    #         f = Buddies(follower=self, following=user)
    #         db.session.add(f)
    #
    # def unfollow(self, user):
    #     f = self.following.filter_by(following_id=user.id).first()
    #     if f:
    #         db.session.delete(f)
    #
    # def is_following(self, user):
    #     return self.following.filter_by(following_id=user.id).first() is not None
    #
    # def is_followed_by(self, user):
    #     return self.followers.filter_by(follower_id=user.id).first() is not None

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('user.login'))
