from django.urls import path
from . import handlers


urlpatterns = [
    path("staff-skills-handler", handlers.staff_skills_handler),
    path("employees-handler", handlers.EmployeesHandler.as_view()),
    path("tasks-handler", handlers.TaskHandler.as_view()),
]
