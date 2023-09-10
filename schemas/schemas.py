from tortoise.contrib.pydantic import pydantic_model_creator
from models import UserInfo, MainInfo

UserInfo_Pydantic = pydantic_model_creator(
    UserInfo, name="UserInfo", exclude=["password"]
)
UserInfoIn_Pydantic = pydantic_model_creator(
    UserInfo, name="UserInfoIn", exclude_readonly=True
)

MainInfo_Pydantic = pydantic_model_creator(MainInfo, name="MainInfo")
MainInfoIn_Pydantic = pydantic_model_creator(
    MainInfo, name="MainInfoIn", exclude_readonly=True
)
