# Generated by Django 4.1.7 on 2023-04-25 21:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("staff_performance_tracking", "0003_staffmember_skills"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"verbose_name": "Task", "verbose_name_plural": "Tasks"},
        ),
        migrations.RemoveField(
            model_name="task",
            name="delivery_date",
        ),
        migrations.AddField(
            model_name="staffmember",
            name="can_accept_tasks",
            field=models.BooleanField(
                default=True, verbose_name="Staff member can accept tasks"
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="due_date",
            field=models.DateField(
                default=django.utils.timezone.now, verbose_name="Due data"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="task",
            name="name",
            field=models.CharField(
                default="task name", max_length=350, verbose_name="Task name"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="task",
            name="assigned_to",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="assigned_to",
                to="staff_performance_tracking.staffmember",
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="description",
            field=models.TextField(verbose_name="Description"),
        ),
        migrations.AlterField(
            model_name="task",
            name="issued_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="issued_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]