from django.db import models
from accounts.models import User
from staff_performance_tracking.models import StaffMember, Task

# Create your models here.


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class ClientProject(models.Model):
    project_name = models.CharField(max_length=100, verbose_name="Project name")
    project_description = models.TextField(verbose_name="Project description")
    proceeded = models.BooleanField(default=False)
    supervisor = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Supervisor", null=True
    )
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    staff_members = models.ManyToManyField(
        StaffMember, verbose_name="Staff members", related_name="staff_members"
    )
    started_at = models.DateTimeField(auto_now_add=True, verbose_name="Started at")

    class Meta:
        verbose_name = "Client project"
        verbose_name_plural = "Client projects"

    def __str__(self):
        return self.project_name


class ClientProjectMilestone(models.Model):
    client_project = models.ForeignKey(
        ClientProject,
        on_delete=models.CASCADE,
        verbose_name="Related client project",
        null=True,
    )
    milestone_name = models.CharField(max_length=100)
    related_tasks = models.ManyToManyField(
        Task, verbose_name="Related tasks", related_name="milestone_tasks"
    )
    description = models.TextField(verbose_name="Milestone description")
    milestone_price = models.FloatField(verbose_name="Milestone price")
    delivery_date = models.DateField(verbose_name="Milestone delivery date")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    proceeded = models.BooleanField(
        default=False, verbose_name="Milestone is proceeded"
    )

    class Meta:
        verbose_name = "Client project milestone"
        verbose_name_plural = "Client project milestones"

    def __str__(self):
        return self.milestone_name


class ScheduledUpdate(models.Model):
    update_name = models.CharField(max_length=255, verbose_name="Update Name")
    release_date = models.DateField(verbose_name="Release Date")
    major_update = models.BooleanField(verbose_name="Major Update")
    release_description = models.TextField(verbose_name="Release Description")

    class Meta:
        verbose_name = "Scheduled Update"
        verbose_name_plural = "Scheduled Updates"

    def __str__(self):
        return self.update_name
