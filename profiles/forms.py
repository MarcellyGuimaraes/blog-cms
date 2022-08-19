from django import forms
from django.forms import ModelForm
from .models import UserProfile

class UpdateProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['usuario']