from django.contrib.auth.views import LogoutView
from django.urls import path, include
from CoockingWebsite.accounts.views import RegisterView, UserLoginView, UserDetailView, UserEditView, UserDeleteView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', UserDetailView.as_view(), name='profile_detail'),
        path('edit/', UserEditView.as_view(), name='edit_profile'),
        path('delete/', UserDeleteView.as_view(), name='delete_profile'),
    ])),
]

