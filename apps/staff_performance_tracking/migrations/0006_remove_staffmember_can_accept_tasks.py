# Generated by Django 4.1.7 on 2023-04-25 21:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("staff_performance_tracking", "0005_task_client_project"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="staffmember",
            name="can_accept_tasks",
        ),
    ]
