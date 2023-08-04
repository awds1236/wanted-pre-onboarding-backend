from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegistrationForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'id': 'email', 'name': 'email'}))
    password = forms.CharField(
        min_length=8, 
        widget=forms.PasswordInput(attrs={'id': 'pswd1', 'name': 'pswd1'})
    )
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not "@" in email:
            raise ValidationError("Invalid email address12")
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email address must be unique12")
        return email

    def save(self):
        User.objects.create_user(
            username=self.cleaned_data.get('email'),
            email=self.cleaned_data.get('email'),
            password=self.cleaned_data.get('password')
        )
