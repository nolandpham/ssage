# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy.dialects.mysql import JSON as MySQLJSON
from sqlalchemy.inspection import inspect

from sage.app import db


class Serializer(object):
    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]


class Product(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1024), nullable=False)
    description = db.Column(db.Text, nullable=True)
    images = db.Column(MySQLJSON, nullable=True)
    logo_id = db.Column(db.Integer, nullable=True)
    created_at = db.Column(DateTime, default=datetime.utcnow)
    updated_at = db.Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<Product %r>' % self.name


class Variant(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    name = db.Column(db.String(1024), nullable=False)
    size = db.Column(db.String(1024), nullable=True)
    color = db.Column(db.String(1024), nullable=True)
    images = db.Column(MySQLJSON, nullable=True)
    created_at = db.Column(DateTime, default=datetime.utcnow)
    updated_at = db.Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<Variant %r>' % self.name


class Image(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(2048), nullable=False) # max length IE like

    def __repr__(self):
        return '<Image %r>' % self.url


"""
CREATE DATABASE ssage;
USE ssage;

CREATE TABLE product (
    id INT(6) AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(1024) NOT NULL,
    description TEXT,
    images JSON,
    logo_id INT(6),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE variant (
    id INT(6) AUTO_INCREMENT PRIMARY KEY,
    product_id INT(6) NOT NULL,
    name VARCHAR(1024) NOT NULL,
    size VARCHAR(1024),
    color VARCHAR(1024),
    images JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE image (
    id INT(6) AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(2048) NOT NULL
);
"""
