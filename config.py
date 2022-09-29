# Flask configurations go in this file so they are not in app/__init__.py

import os

class Config(object):

    # Sensitive information like this should not be hardcoded in the application
    # We can provide a value for SECRET_KEY in an environmental variable
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
