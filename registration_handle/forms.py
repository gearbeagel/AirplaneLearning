# forms.py
from django import forms

class MyForm(forms.Form):
    username = forms.CharField(max_length=100)