from django.urls import path
from . import handlers

urlpatterns = [
    path("clients-data", handlers.ClientsDataHandler.as_view()),
    path("clients-projects", handlers.ClientsProjectsHandler.as_view()),
    path("client-project", handlers.ClientProjectHandler.as_view()),
    path(
        "client-project-milestones", handlers.ClientProjectMilestonesHandler.as_view()
    ),
]
