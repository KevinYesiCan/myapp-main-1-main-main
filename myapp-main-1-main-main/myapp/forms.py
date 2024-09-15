from django import forms
from .models import UserLogin

class LoginForm(forms.ModelForm):
    class Meta:
        model = UserLogin
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
