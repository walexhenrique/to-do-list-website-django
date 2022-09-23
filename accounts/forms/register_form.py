from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterForm(forms.ModelForm):

    username = forms.CharField(
        label='NOME DE USUARIO',
        error_messages= {
            'required': 'Error, username is required',
            'max_length': 'USERNAME is very long',
        },
        max_length=150,
    )

    first_name = forms.CharField(
        label='PRIMEIRO NOME',
        error_messages={
            'required': 'Error, First name is required',
            'max_length': 'First name is very long',
        },
        max_length=150,
    )

    last_name = forms.CharField(
        label='SOBRENOME',
        error_messages={
            'required': 'Error, Last name is required',
            'max_length': 'Last name is very long',
        },
        max_length=150,
    )

    email = forms.EmailField(
        label='EMAIL',
        error_messages={
            'required':'Error, Email is required',
        },
    )

    password = forms.CharField(
        label='SENHA',
        widget=forms.PasswordInput(),
        error_messages={
            'required': 'Error, Password is required',
        }
    )

    password2 = forms.CharField(
        label='REPITA A SUA SENHA',
        widget=forms.PasswordInput(),
        error_messages={
            'required': 'Error, Please repeat your password',
        },
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


    def clean_username(self):
        username = self.cleaned_data.get('username', '')

        username_exists = User.objects.filter(username=username).exists()

        if username_exists:
            raise ValidationError('Username alredy exists in database', code='invalid')
        
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        
        email_exists = User.objects.filter(email=email).exists()

        if email_exists:
            raise ValidationError('Email alredy exists in database', code='invalid')
        
        return email
    
    def clean_password(self):
        password = self.cleaned_data.get('password', '')

        if len(password) < 4:
            raise ValidationError('Error, Password is too short', code='invalid')
        
        return password
    
    def clean_password2(self):
        password2 = self.cleaned_data.get('password2', '')

        if len(password2) < 4:
            raise ValidationError('Error, Password is too short', code='invalid')
        
        return password2
    
    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password', '')
        password2 = cleaned_data.get('password2', '')

        if password != password2:
            raise ValidationError('Error, Passwords not equals', code='invalid')
