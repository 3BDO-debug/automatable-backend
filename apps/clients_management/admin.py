from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Client)
admin.site.register(models.ClientProjectMilestone)
admin.site.register(models.ClientMeeting)
