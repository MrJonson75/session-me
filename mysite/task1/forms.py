from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Имя пользователя')
    password = forms.CharField(max_length=8, widget=forms.PasswordInput(), label='Пароль')
    repeat_password = forms.CharField(max_length=8, widget=forms.PasswordInput(), label='Пароль')
    age = forms.CharField(max_length=3, empty_value=int, label='Возраст')
