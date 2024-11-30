from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, DetailView

from CoockingWebsite.posts.forms import PostAddForm, PostEditForm
from CoockingWebsite.posts.models import Post


# Create your views here.
class AddPost(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostAddForm
    context_object_name = 'posts'
    template_name = 'posts/add_post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'posts/delete_post.html'
    success_url = reverse_lazy('my_recipes')

    def delete(self, request, *args, **kwargs):
        post = self.get_object()
        response = super().delete(request, *args, **kwargs)  # Извиква стандартното изтриване
        # Актуализиране на total_recipes
        user_profile = post.author.profile
        user_profile.total_recipes = post.author.posts.count()
        user_profile.save()
        return response

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class DetailPost(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Post
    context_object_name = 'recipe'
    template_name = 'posts/detail_post.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class EditPost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'posts/edit_post.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def get_success_url(self):
        return reverse_lazy('my_recipes')


class MyRecipesView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/my_recipes.html'
    context_object_name = 'my_recipes'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
