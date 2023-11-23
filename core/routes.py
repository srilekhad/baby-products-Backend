from fastapi import APIRouter

from users.routes import api_router as user_router
from shoping_app.routes import api_router as shoping_app_router


api_router = APIRouter()

api_router.include_router(user_router, prefix="/users")
api_router.include_router(shoping_app_router, prefix="/shoping_app")
