from django.urls import path

from CoockingWebsite.index.views import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
]