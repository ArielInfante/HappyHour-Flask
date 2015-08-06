from . import main
from flask import render_template, flash
from flask.ext.login import logout_user, login_required, current_user
from app import app

@main.route('/', methods=['GET', 'POST'])
@main.route('/index', methods=['GET', 'POST'])
def index():
    if current_user.username != "Guest":
        return render_template('index.html', title="Happy Hour", user=current_user)
    return render_template('index.html', title="Happy Hour", user=False)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(403)
def page_forbidden(error):
    return render_template('403.html'), 403

@app.errorhandler(410)
def page_gone(error):
    return render_template('410.html'), 410

@app.errorhandler(500)
def page_server_error(error):
    return render_template('500.html'), 500