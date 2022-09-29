# This file makes the folder app to be a package

from flask import Flask

# Import class Confic, created in modile config (top level),
# which contains configurations we defined for Flask
from config import Config

# Create an instance of the Flask Class imported from the
# flask package, passing the __name__ special variable
app = Flask(__name__)

# Configure secret key from config.py
app.config.from_object(Config)

# Alternative way not recommended: configure it directly in this file
# app.config['SECRET_KEY'] = 'you-will-never-guess'

# Import routes from app package (the folder containing this file)
# routes is another module that also lives inside this package
from app import routes
