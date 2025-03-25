from fastapi import FastAPI
from app.config import routers, settings

app = FastAPI(title="Night watch fraud service")

app.include_router(
    routers.urls
)
