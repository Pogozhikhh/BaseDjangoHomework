from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUsers


class UserCreationsForm(UserCreationForm):
    email = forms.EmailField(max_length=100, required=True)
    phone_number = forms.CharField(
        max_length=20,
        required=False,
        help_text="Необязательное поле. Введите номер телефона.",
    )
    usable_password = None

    class Meta:
        model = CustomUsers
        fields = [
            "avatar",
            "email",
            "country",
            "phone_number",
            "password1",
            "password2",
        ]
