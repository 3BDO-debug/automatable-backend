from django.db import models
from django.apps import apps
from accounts.models import User, AllowedView
from django.utils.text import slugify

# Create your models here.


class StaffSkill(models.Model):
    name = models.CharField(max_length=350, verbose_name="Skill name")
    slug = models.SlugField(verbose_name="Skill slug", null=True, blank=True)

    class Meta:
        verbose_name = "Staff skill"
        verbose_name_plural = "Staff skills"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(StaffSkill, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class StaffMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    role = models.CharField(max_length=350, verbose_name="Role")
    allowed_views = models.ManyToManyField(
        AllowedView, verbose_name="Allowed views", related_name="allowed_views"
    )
    skills = models.ManyToManyField(
        StaffSkill, verbose_name="Skills", related_name="staff_skills"
    )
    can_accept_tasks = models.BooleanField(
        default=True, verbose_name="Staff member can accept tasks"
    )

    class Meta:
        verbose_name = "Staff member"
        verbose_name_plural = "Staff members"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} -- {self.role}"


class Task(models.Model):
    client_project = models.ForeignKey(
        "clients_management.ClientProject",
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Related client project",
    )
    name = models.CharField(max_length=350, verbose_name="Task name")
    description = models.TextField(verbose_name="Description")
    issued_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="issued_by"
    )
    due_date = models.DateField(verbose_name="Due data")
    assigned_to = models.ForeignKey(
        StaffMember, on_delete=models.CASCADE, related_name="assigned_to", null=True
    )
    is_proceeded = models.BooleanField(default=False, verbose_name="Task is proceeded")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.name


class TaskReview(models.Model):
    reviewed_by = models.ForeignKey(
        StaffMember,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    review_description = models.TextField()
    rating = models.PositiveSmallIntegerField()
    proceeded = models.BooleanField(default=False)

    def __str__(self):
        return f"Review by {self.reviewed_by} with rating {self.rating}"
