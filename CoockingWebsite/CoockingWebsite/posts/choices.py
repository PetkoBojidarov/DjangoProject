from django.db import models


class RecipesCategory(models.TextChoices):
    DESSERT = 'Dessert', 'Dessert'
    BREAKFAST = 'Breakfast', 'Breakfast'
    LUNCH = 'Lunch', 'Lunch'
    DINNER = 'Dinner', 'Dinner'
