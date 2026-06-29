from fastapi import APIRouter
from fastapi.responses import JSONResponse

users_routes = APIRouter(tags=["Usuários"])


@users_routes.get("/users")
async def criar_usuario():
    return JSONResponse(content={"message": "Rota de usuários funcionando!"})