from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="ユーザー名",
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="パスワード",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    error_messages = {
        'invalid_login': "パスワードまたはIdが違います",
        'inactive': "このアカウントは非アクティブです",
    }
