from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField, PasswordChangeForm, PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation

class UserRegistrationFrom(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))

    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))

    password1 = forms.CharField(label='Password' ,required=True, widget=forms.PasswordInput(attrs={'class':'form-control'}))

    password2 = forms.CharField(label='Confirm Password' ,required=True, widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username','email','password1','password1')
        labels = {'email':'Email'} 

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))   

    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput(attrs={'autofocus':'curent-password', 'class':'form-control'}))    


