# -*- coding: utf-8 -*-
from __future__ import absolute_import
from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy.dialects.mysql import JSON as MySQLJSON
from main import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1024), nullable=False)
    description = db.Column(db.Text, nullable=True)
    images = db.Column(MySQLJSON, nullable=True)
    logo_id = db.Column(db.Integer, nullable=True)
    created_at = db.Column(DateTime, default=datetime.utcnow)
    updated_at = db.Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<Product %r>' % self.name

# - id: any type of unique id
# - name: name of the product
# - description: description of the product
# - images: an list of associated images
# - logo_id: the primary logo for this images
# - created_at: timestamp
# - updated_at: timestamp


class Variant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    name = db.Column(db.String(1024), uniquenullable=False)
    size = db.Column(db.String(1024), nullable=True)
    color = db.Column(db.String(1024), nullable=True)
    images = db.Column(MySQLJSON, nullable=True)
    created_at = db.Column(DateTime, default=datetime.utcnow)
    updated_at = db.Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<Variant %r>' % self.name

# - id: any type of unique id
# - product_id: id of the relevant product
# - name: name of the variant
# - size: size of the variant
# - color: color of the variant
# - images: an list of associated images
# - created_at: timestamp
# - updated_at: timestamp


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(2048), nullable=False) # max length IE like

    def __repr__(self):
        return '<Image %r>' % self.url
