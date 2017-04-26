from django import forms
from s3direct.widgets import S3DirectWidget
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm 

class S3DirectUploadForm(forms.Form):
  upload = forms.URLField(widget=S3DirectWidget(dest='misc'))


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


