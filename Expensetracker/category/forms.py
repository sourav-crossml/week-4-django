from django import forms

class CategoryForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)