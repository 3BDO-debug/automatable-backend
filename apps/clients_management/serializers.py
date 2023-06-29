from rest_framework.serializers import ModelSerializer
from accounts.serializers import UserSerializer
from . import models
from staff_performance_tracking.serializers import StaffSkillSerializer


class ClientSerializer(ModelSerializer):
    class Meta:
        model = models.Client
        fields = "__all__"

    def to_representation(self, instance):
        data = super(ClientSerializer, self).to_representation(instance)
        data["account_data"] = UserSerializer(instance.user, many=False).data

        return data


class ClientProjectSerializer(ModelSerializer):
    class Meta:
        model = models.ClientProject
        fields = "__all__"

    def to_representation(self, instance):
        data = super(ClientProjectSerializer, self).to_representation(instance)
        data[
            "supervisor"
        ] = f"{instance.supervisor.first_name} {instance.supervisor.first_name}"
        data["staff_members"] = [
            {
                "fullname": f"{staff_member.user.first_name} {staff_member.user.last_name}",
                "id": staff_member.id,
            }
            for staff_member in instance.staff_members.all()
        ]
        data["team"] = [
            {
                "fullname": f"{staff_member.user.first_name} {staff_member.user.last_name}",
                "skills": [skill.name for skill in staff_member.skills.all()],
            }
            for staff_member in instance.staff_members.all()
        ]
        return data


class ClientProjectMilestoneSerializer(ModelSerializer):
    class Meta:
        model = models.ClientProjectMilestone
        fields = "__all__"
