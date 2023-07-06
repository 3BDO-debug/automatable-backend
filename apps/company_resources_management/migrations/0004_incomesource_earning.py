# Generated by Django 4.1.7 on 2023-07-04 22:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("company_resources_management", "0003_alter_expense_date_issued_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="IncomeSource",
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
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="Income source name"),
                ),
                (
                    "description",
                    models.TextField(verbose_name="Income source description"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
            ],
            options={
                "verbose_name": "Income source",
                "verbose_name_plural": "Income sources",
            },
        ),
        migrations.CreateModel(
            name="Earning",
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
                (
                    "date_recieved",
                    models.DateTimeField(auto_now_add=True, verbose_name="Date issued"),
                ),
                ("price", models.FloatField(verbose_name="Amount due")),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "income_source",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="company_resources_management.incomesource",
                        verbose_name="Related income source",
                    ),
                ),
            ],
            options={
                "verbose_name": "Earning",
                "verbose_name_plural": "Earnings",
            },
        ),
    ]