from fastapi import APIRouter

from app.core.config import settings
# -------- ALL modules import ----------#
from app.modules.auth.router import auth_router
from app.modules.user.router import user_router


api_router = APIRouter()
# Example router import
api_router.include_router(auth_router)
api_router.include_router(user_router)



