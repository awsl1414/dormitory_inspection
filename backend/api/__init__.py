from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from backend.core import settings
from .dormitoryInfo import app01

app = FastAPI(title=settings.TITLE, description=settings.DESC)

app.include_router(app01)

register_tortoise(
    app,
    db_url="sqlite://dormitory.sqlite",
    modules={"models": ["backend.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
