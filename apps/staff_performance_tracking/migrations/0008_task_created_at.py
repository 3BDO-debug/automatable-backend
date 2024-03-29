# Generated by Django 4.1.7 on 2023-04-25 22:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("staff_performance_tracking", "0007_staffmember_can_accept_tasks"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Created at",
            ),
            preserve_default=False,
        ),
    ]
