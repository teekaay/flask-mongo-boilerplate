#!/usr/bin/env python

"""
Script for managing the flask application.
"""

from flask_script import Manager
from app import app

manager = Manager(app)

@manager.command
def hello():
    print('Hello')

if __name__ == '__main__':
    manager.run()