from django import forms
from .models import Posts


class Create(forms.ModelForm):
    class Meta:
        model = Posts
        fields = {'title', 'content'}
