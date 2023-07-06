from django.urls import path
from . import handlers

urlpatterns = [
    path("clients-data", handlers.ClientsDataHandler.as_view()),
    path("client-details", handlers.ClientDetailsHandler.as_view()),
    path("clients-projects", handlers.ClientsProjectsHandler.as_view()),
    path("client-project", handlers.ClientProjectHandler.as_view()),
    path(
        "client-project-milestones", handlers.ClientProjectMilestonesHandler.as_view()
    ),
    path("client-meetings-handler", handlers.ClientMeetingsHandler.as_view()),
    path("scheduled-updates-handler", handlers.ScheduledUpdatesHandler.as_view()),
]
