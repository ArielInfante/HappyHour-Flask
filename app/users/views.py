from . import user
from flask import render_template, redirect, url_for, flash, request, abort, jsonify, json
from app import db
from forms import LoginForm, SignUpForm, EditProfileForm, AvatarForm
from models import User
from app.functions import username_is_valid, email_is_valid, allowed_extensions
from flask.ext.login import login_required, login_user, logout_user, current_user
from werkzeug import secure_filename
from app import csrf
from app import app
import os
from PIL import Image
from base64 import b64decode, decode

@user.route('/signup', methods=['GET', 'POST'])
def signup():

    if not current_user.is_anonymous():
        return redirect(url_for('main.index'))

    form = SignUpForm()

    if form.validate_on_submit():
        # print form.username.data, form.email.data, form.name.data, form.password.data
        # print User.check_email_taken(form.email.data.lower())
        if User.check_email_taken(form.email.data.lower()):
            flash("Email is already taken")
            return render_template('signup.html', form=form)

        # print User.check_username_taken(form.username.data.lower())
        if User.check_username_taken(form.username.data.lower()):
            flash("Username is already taken")
            return render_template('signup.html', form=form)

        user = User(
            form.username.data,
            form.email.data,
            form.name.data,
            form.password.data
        )
        # print dir(user)
        db.session.add(user)
        db.session.commit()

        login_user(user)

        return redirect(url_for('main.index'))
    flash("some error happened")
    return render_template('signup.html', form=form)


@user.route('/login', methods=['GET', 'POST'])
def login():

    if not current_user.is_anonymous():
        return redirect(url_for('main.index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = form.username_email.data
        # print user
        # print form.password.data

        if email_is_valid(user):
            user = User.query.filter_by(email=form.username_email.data.lower()).first()
        else:
            user = User.query.filter_by(username_check=form.username_email.data.lower()).first()

        # print user

        if user is not None and user.verify_password(form.password.data):
            # print user.username
            login_user(user)
            flash('Logged in successfully')
            return redirect(url_for('main.index'))

        flash("Invalid credentials")
        return render_template('login.html', form=form)

    return render_template('login.html', form=form)


@user.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You are being logged out")
    return redirect(url_for('main.index'))


@user.route('/profile')
@login_required
def profile():
    return render_template('ownprofile.html', title=current_user.username, user=current_user)


@user.route('/profile/edit')
@login_required
def editprofile():

    form = EditProfileForm(obj=current_user)

    # form.populate_obj(user)

    if form.validate_on_submit():
        return render_template('editprofile.html', title="Username", user=current_user, form=form)

    return render_template('editprofile.html', title="Username", user=current_user, form=form)


@user.route('/profile/avatar')
@login_required
def upload():
    form = AvatarForm()

    if current_user.avatar is not None:
        return render_template('avatar.html', title="Upload Avatar", user=current_user, form=form, has_avatar=True)
    # if request.method == 'POST':
    #     form_data = request.values
    #
    #     filename = secure_filename(form.photo.data.filename)
        # form.photo.data.save('uploads/' + current_user.get_id() + '/' + filename)
        # return render_template('avatar.html', title="Upload Avatar", user=current_user, form=form)
        # flash("Testing Ajax Calls")
    return render_template('avatar.html', title="Upload Avatar", user=current_user, form=form, has_avatar=False)


@user.route('/profile/avatar/_avatar', methods=['POST'])
def ajax_uploadavatar():
    if request.method == 'POST':
        request_file = request.files['original']
        if request_file and allowed_extensions(request_file.filename):
            users_folder = os.path.join(app.config['UPLOAD_IMG_FOLDER'], current_user.get_id())

            image_name = secure_filename(request_file.filename)
            image_type = request_file.content_type.split('/')[1]

            thumbnail_size = 128, 128
            thumbnail_name = 'thumbnail.' + image_type

            try:
                os.makedirs(users_folder)
            except OSError:
                if not os.path.isdir(users_folder):
                    return jsonify(outcome="fail")

            request_file.save(os.path.join(users_folder, image_name))

            thumbnail_image = Image.open(os.path.join(users_folder, image_name))
            thumbnail_image.thumbnail(thumbnail_size)
            thumbnail_image.save('%s/%s' % (users_folder, thumbnail_name))

            current_user.avatar = image_name
            current_user.thumbnail = thumbnail_name

            User.update()
            return jsonify(outcome="success")
        return jsonify(outcome="fail")
    return jsonify(outcome="fail")


@user.route('/user')
@login_required
def redirect_user():
    # This should be a search feature to find other users
    return redirect(url_for('main.index'))


@user.route('/user/<username>')
@login_required
def usersprofile(username):
    print username
    # Checks if user is anonymous if it is redirect to landingpage
    # if current_user.is_anonymous():
    #     return redirect(url_for('main.index'))

    if User.compare_user_id(current_user, username):
        return redirect(url_for('user.profile'))

    users_profile = User.query.filter_by(username_check=username.lower()).first()
    if users_profile is not None:
        return render_template('usersprofile.html', title=username, user=current_user, users_profile=users_profile)

    return redirect(url_for('main.index'))
