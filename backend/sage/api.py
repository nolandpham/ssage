# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Blueprint, jsonify

from sage.auth import auth

api_route = Blueprint("api_route", __name__, url_prefix='/api/v1')

@api_route.route('/health', methods=['GET'])
@auth.login_required
def health():
    data = {
        "health": "Good doctor!"
    }
    return jsonify(data), 200


@api_route.route('/product', methods=['GET'])
def list_product():
    from sage.models import Product
    products = Product.query.all()
    return jsonify(products), 200
