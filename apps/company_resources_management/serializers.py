from rest_framework.serializers import ModelSerializer
from . import models


class ExpensesSerializers(ModelSerializer):
    class Meta:
        model = models.Expenses
        fields = "__all__"


class IncomeSourceSerializers(ModelSerializer):
    class Meta:
        model = models.IncomeSource
        fields = "__all__"


class IncomeSerializers(ModelSerializer):
    class Meta:
        model = models.Income
        fields = "__all__"


class ProductSerializers(ModelSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"
