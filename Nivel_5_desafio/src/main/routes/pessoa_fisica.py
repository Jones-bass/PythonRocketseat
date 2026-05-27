from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest

from src.main.composer.pessoa_fisica_create_composer import pessoa_fisica_create_composer
from src.main.composer.pessoa_fisica_lister_composer import pessoa_fisica_lister_composer
from src.main.composer.pessoa_fisica_delete_composer import pessoa_fisica_delete_composer

from src.errors.error_handler import handle_errors

pessoa_fisica_route_bp = Blueprint("pessoa_fisica_routes", __name__)

@pessoa_fisica_route_bp.route("/pessoa_fisica", methods=["POST"])
def create_person():
    try:
        http_request = HttpRequest(body=request.json)
        view = pessoa_fisica_create_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
    
@pessoa_fisica_route_bp.route("/pessoa_fisica", methods=["GET"])
def list_pessoa_fisica():
    http_request = HttpRequest()
    view = pessoa_fisica_lister_composer()

    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code

@pessoa_fisica_route_bp.route("/pessoa_fisica/<int:id>", methods=["DELETE"])
def delete_pessoa_fisica(id):
    try:
        http_request = HttpRequest(param={ "id": id })
        view = pessoa_fisica_delete_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code

    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code

