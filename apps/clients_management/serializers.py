from rest_framework.serializers import ModelSerializer
from accounts.serializers import UserSerializer
from . import models
from cloudinary import CloudinaryImage
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
        data[
            "client_name"
        ] = f"{instance.client.user.first_name} {instance.client.user.last_name}"
        return data


class ClientProjectMilestoneSerializer(ModelSerializer):
    class Meta:
        model = models.ClientProjectMilestone
        fields = "__all__"


class ClientMeetingSerializer(ModelSerializer):
    class Meta:
        model = models.ClientMeeting
        fields = "__all__"

    def to_representation(self, instance):
        data = super(ClientMeetingSerializer, self).to_representation(instance)
        print("dasdas", instance.client_project.supervisor.first_name)
        data["supervisor_data"] = {
            "fullname": f"{instance.client_project.supervisor.first_name} {instance.client_project.supervisor.last_name}",
            "profile_pic": CloudinaryImage(
                str(instance.client_project.supervisor.profile_pic)
            ).url,
        }
        data[
            "client_name"
        ] = f"{instance.client_project.client.user.first_name} {instance.client_project.client.user.last_name}"
        return data


class ScheduledUpdateSerializer(ModelSerializer):
    class Meta:
        model = models.ScheduledUpdate
        fields = "__all__"
