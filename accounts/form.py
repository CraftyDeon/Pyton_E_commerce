from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    profile_picture = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'profile_picture']
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']