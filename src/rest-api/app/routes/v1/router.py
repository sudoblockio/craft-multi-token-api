from fastapi import APIRouter
from app.routes.v1.endpoints import craftmultitoken

api_router = APIRouter()
api_router.include_router(craftmultitoken.router, prefix="/craft_multi_token", tags=["craft_multi_token"])
