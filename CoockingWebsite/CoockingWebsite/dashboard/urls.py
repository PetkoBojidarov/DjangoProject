from django.urls import path

from CoockingWebsite.dashboard.views import DashboardView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
]