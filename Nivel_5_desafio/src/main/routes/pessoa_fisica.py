from flask import Blueprint, jsonify
from src.views.http_types.http_request import HttpRequest

from src.main.composer.pessoa_fisica_lister_composer import pessoa_fisica_lister_composer

pessoa_fisica_route_bp = Blueprint("pessoa_fisica_routes", __name__)

@pessoa_fisica_route_bp.route("/pessoa_fisica", methods=["GET"])
def list_pessoa_fisica():
    http_request = HttpRequest()
    view = pessoa_fisica_lister_composer()

    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code
