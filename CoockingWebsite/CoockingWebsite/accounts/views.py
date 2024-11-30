from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from CoockingWebsite.accounts.forms import UserRegistrationForm, UserLoginForm, UserEditForm
from CoockingWebsite.accounts.models import UserProfile


UserModel = get_user_model()


# Create your views here.
class RegisterView(CreateView):
    model = UserModel
    form_class = UserRegistrationForm
    template_name = 'register/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)
        return response


class UserLoginView(LoginView):
    model = UserModel
    form_class = UserLoginForm
    template_name = 'login/login.html'
    success_url = reverse_lazy('home')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')


class UserDetailView(DetailView):
    model = UserProfile
    template_name = 'profile_detail/profile_detail.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



class UserEditView(UpdateView):
    model = UserProfile
    form_class = UserEditForm
    template_name = 'profile_detail/profile_edit.html'
    success_url = reverse_lazy('profile_detail')

    def get_success_url(self):
        return reverse_lazy('profile_detail', kwargs={'pk': self.object.pk})


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = UserModel
    success_url = reverse_lazy('home')

    def test_func(self):
        profile = get_object_or_404(UserProfile, pk=self.kwargs['pk'])
        return self.request.user == profile.user




