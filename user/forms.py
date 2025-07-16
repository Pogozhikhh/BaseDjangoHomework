from django import forms
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

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

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        if phone_number and not phone_number.is_digit():
            raise forms.ValidationError("Номер телефона должен состоять только из цифр")
        return phone_number