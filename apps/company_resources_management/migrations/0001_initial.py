# Generated by Django 4.1.7 on 2023-03-20 09:05

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("release_date", models.DateField()),
                (
                    "subscription_cost",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("description", models.TextField()),
            ],
        ),
    ]
