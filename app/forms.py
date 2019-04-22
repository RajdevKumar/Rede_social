from django import forms
from django.contrib.auth.models import User 
from .models import Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username','password',)
        help_texts = {
            'username':None,
        }
        widgets = {

            'username':forms.TextInput(attrs={
                'class':'formfield',
                'placeholder': 'Username',
                }),

            'first_name':forms.TextInput(attrs={
                'class':'formfield',
                'placeholder': 'Primeiro Nome',
                }),

            'last_name':forms.TextInput(attrs={
                'class':'formfield',
                'placeholder': 'Ultimo Nome',
                }),

            'password':forms.TextInput(attrs={
                'class':'formfield',
                'placeholder': 'password',
                'type':'password',
                }),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('Email','genero',)

        widgets = {
            'Email':forms.TextInput(attrs={
                'class':'formfield',
                'placeholder':'Email',
            }),
        }