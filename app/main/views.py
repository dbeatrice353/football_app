from flask import render_template, session, redirect, url_for, current_app, request
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import LoginForm, RegistrationForm
from .database import DataFetcher
from functools import wraps
from ..models import User
from . import main
from .. import db
import flask



def login_required(f):
    '''Decorator that makes any view function require logging in.'''
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if flask.session.get('user') is None:
            return flask.redirect(flask.url_for('.login'))
        return f(*args, **kwargs)
    return decorated_function


@main.route('/')
def index():
    df = DataFetcher()
    #do cool data stuff here
    return flask.render_template('index.html')

@main.route('/dashboard')
def dashboard():
    return flask.render_template('dashboard.html')

@main.route('/player_profile')
#@login_required
def player_profile():
    #do cool player data stuff here
    return flask.render_template('player_profile.html')

@main.route('/user_profile')
@login_required
def user_profile():
    username = session.get('user')
    #do cool user data stuff here
    return flask.render_template('user_profile.html', user = user)


@main.route('/login', methods = ['GET','POST'])
def login():
   form = LoginForm()
   df = DataFetcher()
   if form.validate_on_submit():
       user = User.query.filter_by(email=form.email.data).first()
       if not user:
           return flask.render_template('login.html', form = form, registered = False)
       pw_hash = user.password_
       if check_password_hash(pw_hash, form.password_.data):
           flask.session['user'] = user.email
           return flask.redirect(flask.url_for('.index'))
   return flask.render_template('login.html', form = form)


@main.route('/register', methods=['GET', 'POST'])
def register():
    duplicate = False
    form = RegistrationForm(flask.request.form)
    form = RegistrationForm()
    if form.validate_on_submit():
        duplicate = User.query.filter_by(email=form.email.data).first()
        if duplicate:
            return flask.render_template('register.html', form=form, duplicate = True)
        user = User()
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.email = form.email.data
        user.password_ = generate_password_hash(form.password_.data)
        db.session.add(user)
        db.session.commit()
        #flask.flash('Thanks for registering')
        return flask.redirect(flask.url_for('.login'))
    return flask.render_template('register.html', form=form)

@main.route('/test')
def test():
    #This is a test view for Kevin so he can be sure his dataabse queries are
    #performnig as planned
    df = DataFetcher()
    data = df.get_average()
    user = session.get('user')
    return flask.render_template('test.html', data = data.to_json(), user = user)
