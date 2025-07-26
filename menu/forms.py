from django import forms
from .models import Category


class Form(forms.ModelForm):

    class Meta:
        model = Category
        fields = ("Category_name", "description")