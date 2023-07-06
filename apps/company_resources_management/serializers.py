from rest_framework.serializers import ModelSerializer
from cloudinary import CloudinaryImage
from . import models


class ExpenseSerializer(ModelSerializer):
    class Meta:
        model = models.Expense  
        fields = "__all__"  

    def to_representation(self, instance):
        data =  super(ExpenseSerializer, self).to_representation(instance)
        data["created_by"] = {
            "fullname" :  f"{instance.created_by.first_name} {instance.created_by.last_name}" ,
            "profile_pic" : CloudinaryImage(str(instance.created_by.profile_pic)).url
        }   

        return data
    


class IncomeSourceSerializer(ModelSerializer):
    class Meta:
        model = models.IncomeSource
        fields = "__all__"

class EarningSerializer(ModelSerializer):
    class Meta:
        model = models.Earning
        fields = "__all__"


    def to_representation(self, instance):
        data =  super(EarningSerializer, self).to_representation(instance)
        data["created_by"] = {
            "fullname" :  f"{instance.created_by.first_name} {instance.created_by.last_name}" ,
            "profile_pic" : CloudinaryImage(str(instance.created_by.profile_pic)).url
        }   
        data["income_source"] = instance.income_source.name

        return data