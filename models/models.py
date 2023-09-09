from enum import IntEnum
from tortoise.models import Model
from tortoise import fields


# class Level(IntEnum):
#     excellent: int = 0
#     qualified: int = 1
#     unqualified: int = 2


class IsAdministrator(IntEnum):
    administrator: int = 0
    not_administrator: int = 1


class UserInfo(Model):
    username = fields.CharField(
        max_length=20, null=False, unique=True, description="用户名"
    )
    password = fields.CharField(max_length=64, null=False, description="密码")
    # is_administrator = fields.IntEnumField(
    #     IsAdministrator, description="是否管理员", default=IsAdministrator.not_administrator
    # )


# class GradeInfo(Model):
#     id = fields.IntField(pk=True, description="年级id")
#     name = fields.CharField(max_length=32, null=False, unique=True, description="年级名称")
#     bedrooms: fields.ForeignKeyRelation["BedroomInfo"]


# class BedroomInfo(Model):
#     id = fields.IntField(pk=True, description="寝室id")
#     name = fields.CharField(max_length=20, null=False, unique=True, description="寝室名称")
#     my_grade: fields.ForeignKeyRelation[GradeInfo] = fields.ForeignKeyField(
#         "models.GradeInfo", related_name="bedrooms", description="所属年级"
#     )
#     rating: fields.ForeignKeyRelation["RatingInfo"]


# class RatingInfo(Model):
#     id = fields.IntField(pk=True, description="id")
#     week_id = fields.IntField(pk=False)
#     week = fields.CharField(max_length=20)
#     rating = fields.CharField(max_length=20)
#     my_bedroom: fields.ForeignKeyRelation[BedroomInfo] = fields.ForeignKeyField(
#         "models.BedroomInfo", related_name="rating", description="所属寝室"
#     )


class MainInfo(Model):
    id = fields.IntField(pk=True)
    grade = fields.CharField(max_length=16, unique=True, null=False, description="年级专业")
    bedroom = fields.CharField(max_length=16, unique=True, null=True, description="宿舍")
    week_id = fields.IntField(pk=False, description="周次")
    weeks = fields.CharField(max_length=16, unique=False, null=False, description="周几")
    rating = fields.CharField(max_length=16, unique=False, null=False, description="评价")
