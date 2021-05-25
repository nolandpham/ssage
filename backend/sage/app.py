# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging
from logging.handlers import RotatingFileHandler

# init Logger
logger = logging.getLogger(__name__)
console_formatter = logging.Formatter(
            '%(levelname)s\t%(filename)s:%(lineno)d\t\t%(message)s', '%m-%d %H:%M:%S')
file_formatter = logging.Formatter(
            '%(levelname)s - %(asctime)s - %(pathname)s - l%(lineno)d - %(message)s', '%m-%d %H:%M:%S')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(console_formatter)

rotatingfile_handler = RotatingFileHandler('backend.log', maxBytes=10000, backupCount=1)
rotatingfile_handler.setLevel(logging.INFO)
rotatingfile_handler.setFormatter(file_formatter)

logger.addHandler(console_handler)
logger.addHandler(rotatingfile_handler)
logger.setLevel(logging.DEBUG)

application = Flask(__name__)

# config database connection
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:root@127.0.0.1:3306/ssage'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(application)

from sage.controllers.product import product_route
from sage.controllers.variant import variant_route
application.register_blueprint(product_route)
application.register_blueprint(variant_route)
