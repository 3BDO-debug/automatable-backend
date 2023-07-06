from django.urls import path
from . import handlers


urlpatterns = [
    path("expenses-handler", handlers.ExpensesHandler.as_view()),
    path("earnings-handler", handlers.EarningsHandler.as_view()),
    path("income-sources-handler", handlers.IncomeSourcesHandler.as_view())
]