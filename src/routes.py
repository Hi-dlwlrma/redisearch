from flask import Blueprint, request, jsonify
from models import Brand

brand_api = Blueprint('brand_api', __name__)
brand_model = Brand()

@brand_api.route('/brands', methods=['POST'])
def add_brand():
    data = request.get_json()
    brand_id = data['id']
    name = data['name']
    result = brand_model.add_brand(brand_id, name)
    return jsonify(result), 201

@brand_api.route('/brands/<brand_id>', methods=['DELETE'])
def delete_brand(brand_id):
    result = brand_model.delete_brand(brand_id)
    return jsonify(result), 200

@brand_api.route('/brands/<brand_id>', methods=['PUT'])
def update_brand(brand_id):
    data = request.get_json()
    name = data['name']
    result = brand_model.update_brand(brand_id, name)
    return jsonify(result), 200

@brand_api.route('/brands/search', methods=['GET'])
def search_brand():
    query = request.args.get('q')
    result = brand_model.search_brand(query)
    return jsonify(result), 200
