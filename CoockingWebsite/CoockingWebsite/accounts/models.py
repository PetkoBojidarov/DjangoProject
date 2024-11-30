from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from CoockingWebsite.accounts.choices import CookingLevelChoices
from CoockingWebsite.accounts.managers import CustomUserManager
from CoockingWebsite.accounts.validators import OnlyLettersValidator


# Create your models here.
class CustomUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(
        unique=True
    )

    is_staff = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


class UserProfile(models.Model):
    user = models.OneToOneField(
        to=CustomUser,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='profile',
    )
    cooking_level = models.CharField(
        max_length=20,
        choices=CookingLevelChoices.choices,
        default=CookingLevelChoices.BEGINNER,
    )

    first_name = models.CharField(
        max_length=30,
        validators=[OnlyLettersValidator()],

    )

    last_name = models.CharField(
        max_length=30,
        validators=[OnlyLettersValidator()],
    )

    favourite_recipes = models.ManyToManyField(
        'posts.Post',
        related_name='favourite_recipes',
        blank=True,
    )

    total_recipes = models.PositiveIntegerField(
        default=0
    )

    profile_image = models.ImageField(
        upload_to='avatars/',
        null=True,
        blank=True,
    )
