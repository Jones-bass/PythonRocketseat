from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.main.composer.user_register_composer import user_register_composer
from src.main.composer.user_finder_composer import user_finder_composer
from src.validators.user_register_validator import UserInput
from src.views.http_types.http_request import HttpRequest


users_routes = APIRouter(tags=["Usuários"])


@users_routes.post("/users")
async def criar_usuario(body: UserInput):
    http_request = HttpRequest(body=dict(body))
    user_register = user_register_composer()
    http_response = await user_register.handle_register_user(http_request)
    return JSONResponse(
        content=http_response.body,
        status_code=http_response.status_code
    )


@users_routes.get("/users/{user_name}")
async def buscar_usuarios_por_nome(user_name: int):
    http_request = HttpRequest(path_params={"user_name": user_name})
    user_finder = user_finder_composer()

    http_response = await user_finder.handle_find_user_by_name(http_request)
    return JSONResponse(
        content=http_response.body,
        status_code=http_response.status_code
    )
    