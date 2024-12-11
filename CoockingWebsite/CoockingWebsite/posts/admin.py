from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CustomUser
from CoockingWebsite.posts.models import Post, Comment, Like
from ..accounts.models import UserProfile


# Регистрация и персонализация на CustomUser
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'is_staff', 'date_joined')
    search_fields = ('email',)
    list_filter = ('is_active', 'is_staff')
    ordering = ('-date_joined',)


# Регистрация и персонализация на UserProfile
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'cooking_level', 'total_recipes')
    search_fields = ('user__email', 'first_name', 'last_name')
    list_filter = ('cooking_level',)


# Регистрация и персонализация на Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at', 'recipes_categories')
    search_fields = ('title', 'author__email', 'ingredients')
    list_filter = ('recipes_categories', 'created_at')
    ordering = ('-created_at',)


# Регистрация и персонализация на Comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'to_recipes', 'text', 'date_time_of_comment')
    search_fields = ('user__email', 'to_recipes__title', 'text')
    list_filter = ('date_time_of_comment',)


# Регистрация и персонализация на Like
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'to_recipes')
    search_fields = ('user__email', 'to_recipes__title')
