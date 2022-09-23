from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label='NOME DE USUARIO')
    password = forms.CharField(widget=forms.PasswordInput(), label='SENHA')
