from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import ListView

from CoockingWebsite.posts.models import Post


class DashboardView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'dashboard/dashboard.html'
    context_object_name = 'recipes'
    paginate_by = 5

    def get_queryset(self):
        queryset = Post.objects.all().order_by('-created_at')
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(Q(title__icontains=query) | Q(description__icontains=query))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_liked_recipes = self.request.user.like_set.values_list('to_recipes', flat=True)
        context['user_liked_recipes'] = user_liked_recipes
        return context
