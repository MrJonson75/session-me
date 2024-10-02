from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


class AddPostForm(forms.ModelForm):
    '''
    Форма отправки поста в блог
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        '''
        Подстановка в поле "Сат" вместо прочерков значения "Категория не выбрана"
        '''
        self.fields['cat'].empty_label = 'Категория не выбрана'


    class Meta:
        model = GamePost
        fields = ['title', 'content', 'photo', 'status', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}, ),
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 10}),

        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 255:
            raise ValidationError('Длина превышает 255 символов')
        return title


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
