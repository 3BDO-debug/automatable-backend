# Generated by Django 4.1.7 on 2023-07-05 21:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clients_management", "0008_clientmeeting"),
    ]

    operations = [
        migrations.AddField(
            model_name="clientmeeting",
            name="client_state",
            field=models.CharField(
                blank=True, max_length=350, null=True, verbose_name="Client state"
            ),
        ),
        migrations.AddField(
            model_name="clientmeeting",
            name="meeting_transcriped",
            field=models.TextField(
                blank=True, null=True, verbose_name="Meeting transcriped"
            ),
        ),
        migrations.AddField(
            model_name="clientmeeting",
            name="sentiment_magnitude",
            field=models.CharField(
                blank=True,
                max_length=350,
                null=True,
                verbose_name="Sentiment magnitude",
            ),
        ),
        migrations.AddField(
            model_name="clientmeeting",
            name="sentiment_score",
            field=models.CharField(
                blank=True, max_length=350, null=True, verbose_name="Sentiment score"
            ),
        ),
    ]
