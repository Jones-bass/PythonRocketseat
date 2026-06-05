from flask import request
from src.drivers.jwt_handler import JwtHandler
from src.errors.error_types.http_unauthorized import HttpUnauthorizedError

def auth_jwt_verify():
    jwt_handle = JwtHandler()
    authorization = request.headers.get("Authorization")

    if not authorization:
        raise HttpUnauthorizedError("Missing authorization token")
  
    token = authorization.replace("Bearer ", "")

    token_infos = jwt_handle.decode_jwt_token(token)

    return token_infos
