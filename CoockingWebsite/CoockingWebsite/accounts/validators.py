from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class OnlyLettersValidator:
    def __call__(self, value):
        if not value.isalpha():
            raise ValidationError('This field can only contain letters!')
