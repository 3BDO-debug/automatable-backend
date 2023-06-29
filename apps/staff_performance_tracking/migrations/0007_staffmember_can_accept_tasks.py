# Generated by Django 4.1.7 on 2023-04-25 21:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("staff_performance_tracking", "0006_remove_staffmember_can_accept_tasks"),
    ]

    operations = [
        migrations.AddField(
            model_name="staffmember",
            name="can_accept_tasks",
            field=models.BooleanField(
                default=True, verbose_name="Staff member can accept tasks"
            ),
        ),
    ]
