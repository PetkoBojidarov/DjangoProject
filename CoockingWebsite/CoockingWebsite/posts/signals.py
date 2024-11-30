from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from CoockingWebsite.posts.models import Post


@receiver(post_save, sender=Post)
def update_total_recipes(sender, instance, created, **kwargs):
    if created:
        # В случай на нова рецепта, актуализираме total_recipes
        user_profile = instance.author.profile  # Вземаме профила на автора
        user_profile.total_recipes = instance.author.posts.count()  # Преброяваме рецептите
        user_profile.save()  # Записваме актуализацията


@receiver(post_delete, sender=Post)
def update_total_recipes_on_delete(sender, instance, **kwargs):
    # При изтриване на рецепта, актуализираме total_recipes
    if instance.author.profile:
        user_profile = instance.author.profile  # Вземаме профила на автора
        user_profile.total_recipes = instance.author.posts.count()  # Преброяваме рецептите
        user_profile.save()  # Записваме актуализацията
