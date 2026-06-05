from flask import Blueprint, jsonify, request

from src.views.http_types.http_request import HttpRequest
from src.main.composer.orders_creator_composer import orders_creator_composer
from src.main.middlewares.auth_middleware import auth_jwt_verify
from src.errors.error_handler import handle_errors

orders_routes_bp = Blueprint("orders_routes", __name__)


@orders_routes_bp.route("/orders", methods=["POST"])
def create_order():
    try:
        token_infos = auth_jwt_verify()

        http_request = HttpRequest(
            body=request.json,
            token_infos=token_infos
        )

        http_response = orders_creator_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
