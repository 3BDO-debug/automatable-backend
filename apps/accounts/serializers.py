from rest_framework.serializers import ModelSerializer
from . import models


class AllowedViewSerializer(ModelSerializer):
    class Meta:
        model = models.AllowedView
        fields = "__all__"


class UserSerializer(ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"
