from typing import Optional
from pydantic import BaseSettings


class Settings(BaseSettings):
    TITLE: Optional[str] = "寝室验收demo"

    DESC: Optional[
        str
    ] = """
    - 寝室验收demo后端部分
    - 实现： FastAPI、tortoise orm ....
    """


settings = Settings()
