from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

from CoockingWebsite.accounts.models import CustomUser, UserProfile


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'placeholder': 'Enter username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter email'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'placeholder': 'Enter password',
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'placeholder': 'Confirm password',
        })

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError('This email is already in use.')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError('This username is already taken.')
        return username


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'placeholder': 'Enter email'}),
        self.fields['password'].widget.attrs.update({'placeholder': 'Enter password'})


class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'total_recipes', 'profile_image', 'cooking_level']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your first name',
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your last name',
        })
        self.fields['total_recipes'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Number of recipes',
            'readonly': 'readonly',  # Ако това поле не трябва да се променя от потребителя
        })
        self.fields['profile_image'].widget.attrs.update({'class': 'form-control'})
        self.fields['profile_image'].widget.clear_checkbox_label = ''  # Скрива етикета "Clear"
        self.fields['profile_image'].widget.initial_text = ''  # Скрива текста "Currently"

        self.fields['cooking_level'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your cooking level',
        })


class UserProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = []
