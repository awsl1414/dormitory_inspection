from typing import List, Optional, Union
from fastapi import APIRouter
from backend.models import Dormitory
from backend.scheams import (
    Response200,
    Response400,
    Dormitory_Pydantic,
    DormitoryIn_Pydantic,
)

app01 = APIRouter()


@app01.get("/queryInfo", response_model=Union[Response200, Response400])
async def queryInfo(limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    data = {
        "total": await Dormitory.all().count(),
        "now": await Dormitory_Pydantic.from_queryset(
            Dormitory.all().offset(skip).limit(limit).order_by("-id")
        ),
    }
    return Response200(data=data)


@app01.post("/receiveInfo")
async def receiveInfo(dormitory_data: DormitoryIn_Pydantic):
    return Response200(
        data=await Dormitory_Pydantic.from_tortoise_orm(
            await Dormitory.create(**dormitory_data.dict())
        )
    )
