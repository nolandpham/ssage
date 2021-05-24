# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import logging
from logging.handlers import RotatingFileHandler

application = Flask(__name__)

from sage.api import api_route
application.register_blueprint(api_route)

# config database connection
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:root@localhost/ssage'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(application)

# Set Logger
log = logging.getLogger(__name__)
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

log.addHandler(console_handler)
log.addHandler(rotatingfile_handler)
log.setLevel(logging.DEBUG)


def run():
    # Start Application
    log.info("start application")
    application.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == '__main__':
    run()
