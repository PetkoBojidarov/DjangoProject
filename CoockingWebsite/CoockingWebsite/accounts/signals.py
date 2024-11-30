from django.db.models.signals import post_save
from django.dispatch import receiver

from CoockingWebsite.accounts.models import CustomUser, UserProfile
from CoockingWebsite.posts.models import Post


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


