from django import forms
from . import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['headline','bio','img']
