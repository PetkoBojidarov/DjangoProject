from django.views.generic import ListView

from CoockingWebsite.posts.models import Post


class DashboardView(ListView):
    model = Post
    template_name = 'dashboard/dashboard.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        queryset = Post.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(title__icontains=query)  # Търсене по заглавие
        return queryset
