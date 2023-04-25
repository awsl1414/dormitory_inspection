from tortoise import models, fields


class Dormitory(models.Model):
    houseNumber = fields.CharField(max_length=32, null=False, description="寝室门牌号")
    evaluation = fields.CharField(
        max_length=64, null=False, default="良好", description="卫生评价"
    )
    remarks = fields.CharField(max_length=256, null=True, description="备注")
