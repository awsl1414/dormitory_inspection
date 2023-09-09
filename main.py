from uvicorn import run
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
from apis import app01
from utils import settings

app = FastAPI(title=settings.TITLE, description=settings.DESC)
app.include_router(app01)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许的域名，["*"]表示允许所有
    allow_credentials=True,  # 是否允许发送 Cookie
    allow_methods=["*"],  # 允许的 HTTP 方法；
    allow_headers=["*"],  # 允许的请求 Header
)

register_tortoise(
    app,
    db_url="sqlite://together3.db",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
if __name__ == "__main__":
    # run("main:app", reload=True)
    run("main:app", host="0.0.0.0", port=5000)
