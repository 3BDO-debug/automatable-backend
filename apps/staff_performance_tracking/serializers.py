from rest_framework.serializers import ModelSerializer
from cloudinary import CloudinaryImage
from . import models


class StaffSkillSerializer(ModelSerializer):
    class Meta:
        model = models.StaffSkill
        fields = "__all__"


class StaffMemberSerializer(ModelSerializer):
    class Meta:
        model = models.StaffMember
        fields = "__all__"

    def to_representation(self, instance):
        data = super(StaffMemberSerializer, self).to_representation(instance)
        data["fullname"] = f"{instance.user.first_name} {instance.user.last_name}"
        data["email"] = instance.user.email
        data["date_joined"] = instance.user.date_joined
        data["skills"] = [skill.name for skill in instance.skills.all()]
        data["allowed_views"] = [
            allowed_view.name for allowed_view in instance.allowed_views.all()
        ]
        return data


class TaskSerializer(ModelSerializer):
    class Meta:
        model = models.Task
        fields = "__all__"

    def to_representation(self, instance):
        data = super(TaskSerializer, self).to_representation(instance)
        data["assigned_to_id"] = instance.assigned_to.id
        data["assigned_to"] = {
            "fullname": f"{instance.assigned_to.user.first_name} {instance.assigned_to.user.last_name}",
            "profile_pic": CloudinaryImage(
                str(instance.assigned_to.user.profile_pic)
            ).url,
        }
        data["client_project_name"] = instance.client_project.project_name
        data[
            "issued_by_name"
        ] = f"{instance.issued_by.first_name} {instance.issued_by.last_name}"
        return data
