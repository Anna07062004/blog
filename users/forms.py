from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

User = get_user_model()

class RegisterFrom(UserChangeForm):
    email = forms.EmailField(label="Email", required=False)

    class Meta:
        model = User
        fields = ["username", "email", "password", "password2"]

        