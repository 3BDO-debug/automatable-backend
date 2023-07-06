# Generated by Django 4.1.7 on 2023-07-05 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("clients_management", "0010_remove_clientmeeting_client_satisfaction"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="clientmeeting",
            name="client",
        ),
        migrations.AddField(
            model_name="clientmeeting",
            name="client_project",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="clients_management.clientproject",
                verbose_name="Client project",
            ),
        ),
    ]