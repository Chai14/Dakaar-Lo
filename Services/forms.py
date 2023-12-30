from django import forms
from .models import Custom

class CustomSection(forms.Form):
    demo = forms.CharField()
    email = forms.EmailField()
