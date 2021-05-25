# -*- coding: utf-8 -*-
from __future__ import absolute_import
from flask import Blueprint, jsonify, Flask, request, jsonify, make_response
from sage.auth import auth

api_route = Blueprint("api_route", __name__, url_prefix='/api/v1')

from main import db
from sage.models import Product


@api_route.route('/health', methods=['GET'])
@auth.login_required
def health():
    data = {
        "health": "Good doctor!"
    }
    return jsonify(data), 200


@api_route.route('/product/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.filter_by(id=id).first()
    if not product:
        return jsonify({'message': 'Product not found.'}), 400

    return jsonify(product.serialize()), 200


@api_route.route('/product', methods=['GET'])
def list_product():
    print(Product.__table__.columns.keys())
    products = Product.query.all()
    return jsonify(Product.serialize_list(products)), 200


@api_route.route('/product', methods=['POST'])
def create_product():
    product = Product()

    if 'name' in request.form:
        product.name = request.form.get('name')
    else:
        return jsonify({'message': 'Product name are required!'}), 400

    product.description = request.form.get('description')
    product.images = request.form.get('images')
    product.logo_id = request.form.get('logo_id')

    # do save
    db.session.add(product)
    db.session.commit()

    return jsonify(product.serialize()), 201


@api_route.route('/product/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.filter_by(id=id).first()
    if not product:
        return jsonify({'message': 'Product not found.'}), 400

    if 'name' in request.form:
        product.name = request.form.get('name')

    if 'description' in request.form:
        product.description = request.form.get('description')

    if 'images' in request.form:
        product.images = request.form.get('images')

    if 'logo_id' in request.form:
        product.logo_id = request.form.get('logo_id')

    db.session.add(product)
    db.session.commit()

    return jsonify(product.serialize()), 200


@api_route.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.filter_by(id=id).first()
    if not product:
        return jsonify({'message': 'Product not found.'}), 400

    db.session.delete(product)
    db.session.commit()

    return {}, 200
