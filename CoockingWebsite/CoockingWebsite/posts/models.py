from django.db import models

from CoockingWebsite.accounts.models import CustomUser
from CoockingWebsite.posts.choices import RecipesCategory


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='posts',
    )

    title = models.CharField(
        max_length=50,
    )

    recipes_images = models.ImageField(
        upload_to='recipe_images/',
        null=True,
        blank=True
    )

    ingredients = models.TextField(
        max_length=200,
    )

    description = models.TextField(
        max_length=2000,
    )

    preparation_time = models.CharField(
        max_length=30,
    )

    recipes_categories = models.CharField(
        max_length=50,
        choices=RecipesCategory.choices,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )


class Comment(models.Model):
    user = models.ForeignKey(
        to=CustomUser,
        on_delete=models.CASCADE,
    )

    to_recipes = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
    )

    text = models.TextField(
        max_length=200,
    )

    date_time_of_comment = models.DateTimeField(
        auto_now_add=True
    )


class Like(models.Model):

    user = models.ForeignKey(
        to=CustomUser,
        on_delete=models.CASCADE,

    )

    to_recipes = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('user', 'to_recipes')
