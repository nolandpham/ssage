# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, Flask, request
from sage.app import db
from sage.models import Product, Image

product_route = Blueprint("product_route", __name__, url_prefix='/api/v1')


@product_route.route('/health', methods=['GET'])
def health():
    data = {
        "health": "Good doctor!"
    }
    return jsonify(data), 200


@product_route.route('/product/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.filter_by(id=id).first()
    if not product:
        return jsonify({'message': 'Product not found.'}), 400

    return jsonify(product.serialize()), 200


@product_route.route('/product', methods=['GET'])
def list_product():
    products = Product.query.all()
    return jsonify(Product.serialize_list(products)), 200


@product_route.route('/product', methods=['POST'])
def create_product():
    product = Product()

    if 'name' in request.form:
        product.name = request.form.get('name')
    else:
        return jsonify({'message': 'Product name are required!'}), 400

    product.description = request.form.get('description')
    # product.images = request.form.get('images')
    product.logo_id = request.form.get('logo_id')

    # do save
    db.session.add(product)
    db.session.commit()

    return jsonify(product.serialize()), 201


@product_route.route('/product/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.filter_by(id=id).first()
    if not product:
        return jsonify({'message': 'Product not found.'}), 400

    if 'name' in request.form:
        product.name = request.form.get('name')

    if 'description' in request.form:
        product.description = request.form.get('description')

    # if 'images' in request.form:
    #     product.images = request.form.get('images')

    if 'logo_id' in request.form:
        product.logo_id = request.form.get('logo_id')

    db.session.add(product)
    db.session.commit()

    return jsonify(product.serialize()), 200


@product_route.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.filter_by(id=id).first()
    if not product:
        return jsonify({'message': 'Product not found.'}), 400

    db.session.delete(product)
    db.session.commit()

    return {}, 200


@product_route.route('/product/<int:id>/image', methods=['POST'])
def inject_image(id):
    product = Product.query.filter_by(id=id).first()
    if not product:
        return jsonify({'message': 'Product not found.'}), 400
    
    image = Image()

    if 'url' in request.form:
        image.url = request.form.get('url')

    db.session.add(image)
    db.session.flush()
    print("Created image: %d" % image.id)
    
    # do update variant.images
    images = [image.id]
    if product.images:
        for img_id in product.images:
            images.append(img_id)
    product.images = images
    db.session.add(product)

    db.session.commit()

    return jsonify(product.serialize()), 200
