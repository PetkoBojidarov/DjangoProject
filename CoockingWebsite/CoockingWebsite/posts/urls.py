from django.urls import path, include

from CoockingWebsite.posts import views
from CoockingWebsite.posts.views import AddPost, DeletePost, MyRecipesView, EditPost, DetailPost

urlpatterns = [
    path('add/', AddPost.as_view(), name='add_post'),
    path('my_recipes/', MyRecipesView.as_view(), name='my_recipes'),
    path('post/<int:pk>/', include([
        path('delete/', DeletePost.as_view(), name='delete_post'),
        path('edit/', EditPost.as_view(), name='edit_post'),
        path('detail', DetailPost.as_view(), name='detail_post'),
    ])),
    path('<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('recipe/<int:recipe_id>/like/', views.toggle_like, name='toggle_like'),
]
