from enum import Enum
from typing import Any
from pydantic import BaseModel, Field


class CodeEnum(int, Enum):
    """业务状态码"""

    SUCCESS = 200
    FAIL = 400


class ResponseBasic(BaseModel):
    code: CodeEnum = Field(
        default=CodeEnum.SUCCESS, description="业务状态码 200 是成功, 400 是失败"
    )
    data: Any = Field(default=None, description="数据结果")
    msg: str = Field(default="请求成功", description="提示")


class Response200(ResponseBasic):
    pass


class Response400(ResponseBasic):
    code: CodeEnum = CodeEnum.FAIL
    msg: str = "请求失败"


class ResponseToken(Response200):
    access_token: str
    token_type: str = Field(default="bearer")
