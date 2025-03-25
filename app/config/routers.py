from fastapi import APIRouter
from app.api.v1 import views as api_v1
from app.api.meta import views as meta

urls = APIRouter()

urls.include_router(
    meta.router,
    prefix=""
)

urls.include_router(
    api_v1.router,
    prefix="/api/v1"
)
