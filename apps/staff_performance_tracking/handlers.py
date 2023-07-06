import json
from dateutil.parser import parse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from accounts.models import User, AllowedView
from clients_management.models import ClientProject
import cloudinary.uploader
from . import models, serializers


@api_view(["GET"])
def staff_skills_handler(request):
    skills = models.StaffSkill.objects.all()
    skills_serializer = serializers.StaffSkillSerializer(skills, many=True)

    return Response(status=status.HTTP_200_OK, data=skills_serializer.data)


class EmployeesHandler(APIView):
    def get(self, request):
        employees = models.StaffMember.objects.all().order_by("-user__date_joined")
        employees_serializer = serializers.StaffMemberSerializer(employees, many=True)

        return Response(status=status.HTTP_200_OK, data=employees_serializer.data)

    def post(self, request):
        request_data = json.loads(request.data.get("values"))
        profile_pic = request.FILES.get("profilePic")

        skills = [skill.get("id") for skill in request_data.get("skills")]
        allowed_views = [
            allowed_view.get("id") for allowed_view in request_data.get("allowedViews")
        ]

        user_obj = User.objects.create_user(
            first_name=request_data.get("firstName"),
            last_name=request_data.get("lastName"),
            email=request_data.get("email"),
            username=request_data.get("userName"),
            phone_number=request_data.get("phoneNumber"),
            gov_id="Dummy for now",
            account_type="employee",
            profile_pic=profile_pic,
        )

        """ Create staff member model obj """

        staff_member_obj = models.StaffMember.objects.create(
            user=user_obj, role=request_data.get("role")
        )

        staff_member_obj.allowed_views.set(allowed_views)
        staff_member_obj.skills.set(skills)

        """ Save the staff memeber obj and user obj """

        staff_member_obj.save()
        user_obj.save()

        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request):
        employee_id = int(request.query_params.get("employeeId"))

        employee = models.StaffMember.objects.get(id=employee_id)
        user_obj = User.objects.get(id=employee.user.id)

        """ Delete the main user obj """
        user_obj.delete()

        return Response(status=status.HTTP_200_OK)


class TaskHandler(APIView):
    def get(self, request):
        client_project_id = request.query_params.get("clientProjectId")
        employee_id = request.query_params.get("employeeId")
        if client_project_id:
            client_project = ClientProject.objects.get(id=int(client_project_id))
            tasks = models.Task.objects.filter(client_project=client_project)
            tasks_serializer = serializers.TaskSerializer(tasks, many=True)
        elif employee_id:
            employee = models.StaffMember.objects.get(id=int(employee_id))
            tasks = models.Task.objects.filter(assigned_to=employee)
            tasks_serializer = serializers.TaskSerializer(tasks, many=True)
        else:
            tasks = models.Task.objects.all().order_by("-created_at")
            tasks_serializer = serializers.TaskSerializer(tasks, many=True)

        return Response(status=status.HTTP_200_OK, data=tasks_serializer.data)

    def post(self, request):
        client_project = ClientProject.objects.get(
            id=int(request.data.get("clientProjectId"))
        )
        team_members = client_project.staff_members.all()
        required_skills = {
            (required_skill.get("id"))
            for required_skill in request.data.get("requiredSkills")
        }

        for team_member in team_members:
            team_member_skils = [
                team_member_skill.id for team_member_skill in team_member.skills.all()
            ]
            if (
                required_skills.intersection(team_member_skils) and team_member.can_accept_tasks
            ):

                models.Task.objects.create(
                    client_project=client_project,
                    name=request.data.get("taskName"),
                    description=request.data.get("description"),
                    issued_by=request.user,
                    due_date=parse(request.data.get("dueDate")),
                    assigned_to=team_member,
                ).save()

                print("here")


                team_member.can_accept_tasks = False
                team_member.save()

                return Response(status=status.HTTP_200_OK)

        return Response(
            status=status.HTTP_200_OK,
            data={"task_assign_failed": "Couldn't assign task to team member"},
        )


@api_view(["POST"])
def task_submission_handler(request):
    submission = request.FILES.get("file")
    task_id = request.data.get("taskId")
    
    task = models.Task.objects.get(id=int(task_id))
    upload_response = cloudinary.uploader.upload(
                submission,
                resource_type='raw'
    )
    task.task_submission = upload_response['url']

    task.status = "Task Submitted"

    task.save()

    return Response(status=status.HTTP_200_OK)


@api_view(["GET"])
def tasks_submissions_handler(request):
    tasks = models.Task.objects.filter(is_proceeded=False).exclude(task_submission__isnull=True)
    tasks_serializer = serializers.TaskSerializer(tasks, many=True)

    return Response(status=status.HTTP_200_OK, data=tasks_serializer.data)


@api_view(["POST"])
def task_submission_action_handler(request):
    action = request.data.get("action")
    task = models.Task.objects.get(id=int(request.data.get("taskId")))


    if action == "Submission Accepted":
        task.is_proceeded = True
        task.status = "Submission Accepted"
        team_member = task.assigned_to
        team_member.can_accept_tasks = True
        team_member.save()
    else:
        task.is_proceeded = False
        task.status = "Submission Declined"

    task.save()

    return Response(status=status.HTTP_200_OK)