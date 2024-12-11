from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from CoockingWebsite.posts.models import Post


@receiver(post_save, sender=Post)
def update_total_recipes(sender, instance, created, **kwargs):
    if created:

        user_profile = instance.author.profile
        user_profile.total_recipes = instance.author.posts.count()
        user_profile.save()


@receiver(post_delete, sender=Post)
def update_total_recipes_on_delete(sender, instance, **kwargs):

    if instance.author.profile:
        user_profile = instance.author.profile
        user_profile.total_recipes = instance.author.posts.count()
        user_profile.save()
