from .models import Post
from django import forms
from django.forms import ModelForm

class PosteForm(forms.ModelForm):
 class Meta:
    model = Post
    fields = '__all__'
