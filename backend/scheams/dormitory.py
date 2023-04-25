from tortoise.contrib.pydantic import pydantic_model_creator
from backend.models import Dormitory

Dormitory_Pydantic = pydantic_model_creator(Dormitory, name="dormitory")
DormitoryIn_Pydantic = pydantic_model_creator(
    Dormitory, name="dormitoryIn", exclude_readonly=True
)
