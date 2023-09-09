import json
from typing import List
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from utils import (
    get_password_hash,
    verify_password,
    create_access_token,
    get_current_user,
)
from models import UserInfo, MainInfo
from utils import Response200, Response400, ResponseToken

from schemas import (
    UserInfo_Pydantic,
    UserInfoIn_Pydantic,
    MainInfo_Pydantic,
    MainInfoIn_Pydantic,
)

app01 = APIRouter()


@app01.get("/")
def hello():
    return "hello"


@app01.post("/token", summary="获取token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if user := await UserInfo.get(username=form_data.username):
        token = create_access_token({"sub": user.username})
        return ResponseToken(
            data={"token": f"beadict数据转化成json数据rer {token}"}, access_token=token
        )
    return Response200()


@app01.post("/user", summary="用户新增")
async def user_create(username: str, password: str):
    if await UserInfo.filter(username=username):
        return Response400(msg="用户已存在.")
    return Response200(
        data=await UserInfoIn_Pydantic.from_tortoise_orm(
            await UserInfo.create(username=username, password=password)
        )
    )


@app01.get("/user", summary="当前用户")
async def user_info(user_obj: UserInfo = Depends(get_current_user)):
    """
    - username: str 必传
    - password: str 必传
    """
    return Response200(data=await UserInfo_Pydantic.from_tortoise_orm(user_obj))


@app01.get("/main/query", summary="查询全部信息")
async def main_query(page: int = 1, limit: int = 10):
    skip = (page - 1) * limit
    return await MainInfo_Pydantic.from_queryset(
        MainInfo.all().offset(skip).limit(limit)
    )


@app01.post("/main/add", summary="添加信息")
async def main_add(data: MainInfoIn_Pydantic):
    main_obj = await MainInfo.create(**data.dict(exclude_unset=True))
    return await MainInfo_Pydantic.from_tortoise_orm(main_obj)
