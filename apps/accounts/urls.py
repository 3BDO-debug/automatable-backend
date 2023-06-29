from django.urls import path
from . import handlers

urlpatterns = [
    path("allowed-views-handler", handlers.allowed_views_handler),
    path("logout", handlers.logout_handler),
    path("user-details", handlers.user_details_handler),
]
