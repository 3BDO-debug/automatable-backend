# Generated by Django 4.1.7 on 2023-04-25 22:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("staff_performance_tracking", "0008_task_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="is_proceeded",
            field=models.BooleanField(default=False, verbose_name="Task is proceeded"),
        ),
    ]