# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Blueprint, jsonify
from sage.models import Product

from sage.auth import auth

api_route = Blueprint("api", __name__, url_prefix='/api/v1')

@api.route('/health', methods=['GET'])
@auth.login_required
def health():
    data = {
        "health": "Good doctor!"
    }
    return jsonify(data), 200


@api.route('/product/list', methods=['GET'])
def list_product():
    products = Product.query.all()
    return jsonify(products), 200
