from django import forms
from .models import UserProfile, User
from django.contrib.auth.forms import UserCreationForm
import re

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя',
                               help_text='Имя не должно содержать спец. символов (!@#$%^&*()_+{}|:<>?~).')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def clean_name(self, username):
        if re.search(r"[!@#$%^&*()_+{}|:<>?~]", username):
            raise forms.ValidationError('Ваше имя не должно содержать спец. символов (!@#$%^&*()_+{}|:<>?~).')
        return username