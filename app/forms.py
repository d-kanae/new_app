from django import forms
# from.models import Message,Group,Friend,Good
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django.contrib.auth import get_user_model
User = get_user_model()


class AccountAddForm(forms.Form):
    # """アカウント登録"""
    username = forms.CharField(
        required=True,
        min_length=3,
        max_length=16,
        widget=forms.TextInput(
            attrs={
                'placeholder': ''
            }
        )
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'your-email@example.com'
            }
        )
    )
    password = forms.CharField(
        required=True,
        max_length=255,
        min_length=6,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '******',
            }
        )
    )
    confirm_password = forms.CharField(
        required=True,
        max_length=255,
        min_length=6,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '******',
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise ValidationError('既に登録されているメールアドレスです。')
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        return password

    def clean_confirm_password(self):
        confirm_password = self.cleaned_data['confirm_password']
        return confirm_password

    def clean(self):
        cleaned_data = super().clean()
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            self.add_error(
                field='confirm_password',
                error=ValidationError('パスワードが一致しません。'))
        return cleaned_data
