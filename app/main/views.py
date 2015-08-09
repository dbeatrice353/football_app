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

@main.route('/player_profile')
@login_required
def player_profile():
    #do cool player data stuff here
    return flask.render_template('player_profile.html')

@main.route('/user_profile')
@login_required
def user_profile():
    username = session.get('username')
    #do cool user data stuff here
    return flask.render_template('user_profile.html')


@main.route('/login', methods = ['GET','POST'])
def login():
   form = LoginForm()
   df = DataFetcher()
   if form.validate_on_submit():
       pw_hash = df.get_pw_hash(form.name.data)
       if check_password_hash(pw_hash, form.password.data):
           flask.session['user'] = form.name.data
           return flask.redirect(flask.url_for('.index'))
   return flask.render_template('login.html', form = form)


@main.route('/register', methods=['GET', 'POST'])
def register():
    duplicate = False
    form = RegistrationForm(flask.request.form)
    if form.validate_on_submit():
        user = User()
        #if duplicate:
            #return flask.render_template('register.html', form=form, duplicate = True)
        user.username = form.username.data
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.email = form.email.data
        user.password_ = generate_password_hash(form.password_.data)
        db.session.add(user)
        db.session.commit()
        #flask.flash('Thanks for registering')
        return flask.redirect(flask.url_for('login'))
    return flask.render_template('register.html', form=form)
