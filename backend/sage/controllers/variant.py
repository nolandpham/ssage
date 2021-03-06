# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, Flask, request
from sage.app import db
from sage.models import Variant, Image

variant_route = Blueprint("variant_route", __name__, url_prefix='/api/v1')


@variant_route.route('/product/<int:product_id>/variant/<int:id>', methods=['GET'])
def get_variant(product_id, id):
    variant = Variant.query.filter_by(product_id=product_id, id=id).first()
    if not variant:
        return jsonify({'message': 'Variant not found.'}), 400

    return jsonify(variant.serialize()), 200


@variant_route.route('/product/<int:product_id>/variant', methods=['GET'])
def list_variant(product_id):
    variants = Variant.query.filter_by(product_id=product_id).all()
    return jsonify(Variant.serialize_list(variants)), 200


@variant_route.route('/product/<int:product_id>/variant', methods=['POST'])
def create_variant(product_id):
    variant = Variant()
    variant.product_id = product_id

    if 'name' in request.form:
        variant.name = request.form.get('name')
    else:
        return jsonify({'message': 'Variant name are required!'}), 400

    variant.size = request.form.get('size')
    variant.color = request.form.get('color')
    # variant.images = request.form.get('images')

    # do save
    db.session.add(variant)
    db.session.commit()

    return jsonify(variant.serialize()), 201


@variant_route.route('/product/<int:product_id>/variants', methods=['POST'])
def create_variants(product_id):
    variants = []
    variant_data = request.get_json();
    for data in variant_data:
        variant = Variant()
        variant.product_id = product_id

        if 'name' in data:
            variant.name = data['name']
        else:
            return jsonify({'message': 'Variant name are required!'}), 400

        variant.size = data['size']
        variant.color = data['color']
        # variant.images = data['images']

        # do save
        db.session.add(variant)
        variants.append(variant)

    # commit session
    db.session.commit()

    return jsonify(Variant.serialize_list(variants)), 201


@variant_route.route('/product/<int:product_id>/variant/<int:id>', methods=['PUT'])
def update_variant(product_id, id):
    variant = Variant.query.filter_by(product_id=product_id, id=id).first()
    if not variant:
        return jsonify({'message': 'Variant not found.'}), 400

    if 'name' in request.form:
        variant.name = request.form.get('name')

    if 'size' in request.form:
        variant.size = request.form.get('size')

    if 'color' in request.form:
        variant.color = request.form.get('color')

    # if 'images' in request.form:
    #     variant.images = request.form.get('images')

    db.session.add(variant)
    db.session.commit()

    return jsonify(variant.serialize()), 200


@variant_route.route('/product/<int:product_id>/variant/<int:id>', methods=['DELETE'])
def delete_variant(product_id, id):
    variant = Variant.query.filter_by(product_id=product_id, id=id).first()
    if not variant:
        return jsonify({'message': 'Variant not found.'}), 400

    db.session.delete(variant)
    db.session.commit()

    return {}, 200


@variant_route.route('/product/<int:product_id>/variant/<int:id>/image', methods=['POST'])
def inject_image(product_id, id):
    variant = Variant.query.filter_by(product_id=product_id, id=id).first()
    if not variant:
        return jsonify({'message': 'Variant not found.'}), 400
    
    image = Image()

    if 'url' in request.form:
        image.url = request.form.get('url')

    db.session.add(image)
    db.session.flush()
    print("Created image: %d" % image.id)
    
    # do update variant.images
    images = [image.id]
    if variant.images:
        for img_id in variant.images:
            images.append(img_id)
    variant.images = images
    db.session.add(variant)

    db.session.commit()

    return jsonify(variant.serialize()), 200
