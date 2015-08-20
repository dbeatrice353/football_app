import os
from app import create_app, db
from flask.ext.script import Manager
from flask.ext.triangle import Triangle

app = create_app('default')
Triangle(app) # make jinja compatible wwith AngularJS
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
