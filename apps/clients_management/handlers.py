from dateutil.parser import parse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers
from accounts.models import User
from .client_satisfaction_detector import *
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

# Create your views here.


class ClientsDataHandler(APIView):
    def get(self, request):
        clients = models.Client.objects.all().order_by("-created_at")
        clients_serializer = serializers.ClientSerializer(clients, many=True)

        return Response(status=status.HTTP_200_OK, data=clients_serializer.data)

    def post(self, request):
        first_name = request.data.get("firstName")
        last_name = request.data.get("lastName")
        email = request.data.get("email")
        username = request.data.get("userName")
        phone_number = request.data.get("phoneNumber")
        password = request.data.get("password")
        gov_id = request.data.get("govId")

        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            phone_number=phone_number,
            password=password,
            gov_id=gov_id,
            account_type="client",
        )

        models.Client.objects.create(user=user).save()

        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request):
        client_id = int(request.GET.get("clientId"))

        models.Client.objects.get(id=client_id).delete()

        return Response(status=status.HTTP_200_OK)


class ClientDetailsHandler(APIView):
    def get(self, request):
        client_id = int(request.query_params.get("clientId"))

        client = models.Client.objects.get(id=client_id)
        client_serializer = serializers.ClientSerializer(client, many=False)

        return Response(status=status.HTTP_200_OK, data=client_serializer.data)

    def put(self, request):
        client = models.Client.objects.get(id=int(request.data.get("clientId")))
        related_user = client.user

        first_name = request.data.get("firstName")
        last_name = request.data.get("lastName")
        email = request.data.get("email")
        phone_number = request.data.get("phoneNumber")
        gov_id = request.data.get("govId")

        """ Update the client instance """
        related_user.first_name = first_name
        related_user.last_name = last_name
        related_user.email = email
        related_user.phone_number = phone_number
        related_user.gov_id = gov_id

        related_user.save()

        client_serializer = serializers.ClientSerializer(client, many=False)

        return Response(status=status.HTTP_200_OK, data=client_serializer.data)


class ClientsProjectsHandler(APIView):
    def get(self, request):
        clients_projects = models.ClientProject.objects.all().order_by("-started_at")
        clients_projects_serializer = serializers.ClientProjectSerializer(
            clients_projects, many=True
        )

        return Response(
            status=status.HTTP_200_OK, data=clients_projects_serializer.data
        )

    def post(self, request):
        staff_members = [
            staff_member.get("id") for staff_member in request.data.get("teamMembers")
        ]
        client_project_obj = models.ClientProject.objects.create(
            project_name=request.data.get("projectName"),
            project_description=request.data.get("description"),
            supervisor=request.user,
            client=models.Client.objects.get(id=int(request.data.get("clientId"))),
        )

        client_project_obj.staff_members.set(staff_members)

        client_project_obj.save()

        return Response(status=status.HTTP_200_OK)

    def delete(self, request):
        client_project_id = request.query_params.get("clientProjectId")
        models.ClientProject.objects.get(id=int(client_project_id)).delete()

        return Response(status=status.HTTP_200_OK)


class ClientProjectHandler(APIView):
    def get(self, request):
        client_project = models.ClientProject.objects.get(
            id=int(request.query_params.get("clientProjectId"))
        )

        client_project_serializer = serializers.ClientProjectSerializer(
            client_project, many=False
        )

        return Response(status=status.HTTP_200_OK, data=client_project_serializer.data)


class ClientProjectMilestonesHandler(APIView):
    def get(self, request):
        client_project = models.ClientProject.objects.get(
            id=int(request.query_params.get("clientProjectId"))
        )

        milestones = models.ClientProjectMilestone.objects.filter(
            client_project=client_project
        ).order_by("-created_at")

        milestones_serializer = serializers.ClientProjectMilestoneSerializer(
            milestones, many=True
        )

        return Response(status=status.HTTP_200_OK, data=milestones_serializer.data)

    def post(self, request):
        client_project = models.ClientProject.objects.get(
            id=int(request.data.get("clientProjectId"))
        )
        milestone_tasks = [
            task.get("id") for task in request.data.get("milestoneTasks")
        ]

        milestone_obj = models.ClientProjectMilestone.objects.create(
            client_project=client_project,
            milestone_name=request.data.get("name"),
            description=request.data.get("description"),
            milestone_price=float(request.data.get("price")),
            delivery_date=parse(request.data.get("dueDate")),
            proceeded=False,
        )

        milestone_obj.related_tasks.set(milestone_tasks)
        milestone_obj.save()

        return Response(status=status.HTTP_200_OK)


class ScheduledUpdatesHandler(APIView):
    def get(self, request):
        scheduled_updates = models.ScheduledUpdate.objects.all()
        scheduled_updates_serializer = serializers.ScheduledUpdateSerializer(
            scheduled_updates, many=True
        )

        return Response(
            status=status.HTTP_200_OK, data=scheduled_updates_serializer.data
        )

    def post(self, request):
        serializer = serializers.ScheduledUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientMeetingsHandler(APIView):
    def get(self, request):
        client_project = models.ClientProject.objects.get(
            id=int(request.GET.get("clientProjectId"))
        )
        client_meetings = models.ClientMeeting.objects.filter(
            client_project=client_project
        ).order_by("-timestamp")
        client_meetings_serializer = serializers.ClientMeetingSerializer(
            client_meetings, many=True
        )

        return Response(status=status.HTTP_200_OK, data=client_meetings_serializer.data)

    def post(self, request):
        client_project = models.ClientProject.objects.get(
            id=int(request.data.get("clientProjectId"))
        )
        audio_file = request.FILES.get("file")
        description = request.data.get("description")

        audio_file_name = default_storage.save(
            "tmp/" + audio_file.name, ContentFile(audio_file.read())
        )
        audio_file_path = os.path.join(settings.MEDIA_ROOT, audio_file_name)

        text = transcribe_audio_file(audio_file_path)
        sentiment_score, sentiment_magnitude = analyze_sentiment_of_text(text)

        # Clean up the temporary file if one was created
        if audio_file.multiple_chunks():
            default_storage.delete(audio_file_name)

        text = transcribe_audio_file(audio_file_path)
        sentiment_score, sentiment_magnitude = analyze_sentiment_of_text(text)

        if sentiment_score > 0.2 and sentiment_magnitude > 0.2:
            state = "Happy"
        elif sentiment_score < -0.2 and sentiment_magnitude > 0.2:
            state = "Sad"
        else:
            state = "Neutral"

        """ Create client  """

        models.ClientMeeting.objects.create(
            client_project=client_project,
            description=description,
            client_state=state,
            sentiment_score=sentiment_score,
            sentiment_magnitude=sentiment_magnitude,
            meeting_transcriped=text,
        ).save()

        return Response(status=status.HTTP_200_OK)
