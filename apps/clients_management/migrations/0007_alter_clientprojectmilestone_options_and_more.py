# Generated by Django 4.1.7 on 2023-04-25 23:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("staff_performance_tracking", "0009_task_is_proceeded"),
        ("clients_management", "0006_clientproject_supervisor"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="clientprojectmilestone",
            options={
                "verbose_name": "Client project milestone",
                "verbose_name_plural": "Client project milestones",
            },
        ),
        migrations.RenameField(
            model_name="clientprojectmilestone",
            old_name="title",
            new_name="milestone_name",
        ),
        migrations.AddField(
            model_name="clientprojectmilestone",
            name="client_project",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="clients_management.clientproject",
                verbose_name="Related client project",
            ),
        ),
        migrations.AddField(
            model_name="clientprojectmilestone",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Created at",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="clientprojectmilestone",
            name="proceeded",
            field=models.BooleanField(
                default=False, verbose_name="Milestone is proceeded"
            ),
        ),
        migrations.AddField(
            model_name="clientprojectmilestone",
            name="related_tasks",
            field=models.ManyToManyField(
                related_name="milestone_tasks",
                to="staff_performance_tracking.task",
                verbose_name="Related tasks",
            ),
        ),
        migrations.AlterField(
            model_name="clientprojectmilestone",
            name="delivery_date",
            field=models.DateField(verbose_name="Milestone delivery date"),
        ),
        migrations.AlterField(
            model_name="clientprojectmilestone",
            name="description",
            field=models.TextField(verbose_name="Milestone description"),
        ),
        migrations.AlterField(
            model_name="clientprojectmilestone",
            name="milestone_price",
            field=models.FloatField(verbose_name="Milestone price"),
        ),
    ]
