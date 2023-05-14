from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    model = User
    fields = ('username', 'password1', 'password2')

    username = forms.CharField(label="Enter Username :", widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                                'class': 'form-control form-control-lg',
                                                                }))
    password1 = forms.CharField(label="Enter Password :",widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                'class': 'form-control form-control-lg',
                                                                }))
    password2 = forms.CharField(label="Confirm Password :",widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                'class': 'form-control form-control-lg',
                                                                }))
    

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                                'class': 'form-control form-control-lg',
                                                                }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                'class': 'form-control form-control-lg',
                                                                }))