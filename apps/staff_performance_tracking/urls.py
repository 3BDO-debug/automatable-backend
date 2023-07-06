from django.urls import path
from . import handlers


urlpatterns = [
    path("staff-skills-handler", handlers.staff_skills_handler),
    path("employees-handler", handlers.EmployeesHandler.as_view()),
    path("tasks-handler", handlers.TaskHandler.as_view()),
    path("task-submission-handler", handlers.task_submission_handler),
    path("tasks-submissions-handler", handlers.tasks_submissions_handler),
    path("task-submission-action-handler", handlers.task_submission_action_handler)

]
