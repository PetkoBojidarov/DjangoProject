from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, TemplateView

from CoockingWebsite.accounts.models import UserProfile
from CoockingWebsite.posts.models import Post


# Create your views here.
class HomePage(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipes = Post.objects.all().order_by('-created_at')[:3]
        context['user'] = self.request.user
        context['recipes'] = recipes
        return context
