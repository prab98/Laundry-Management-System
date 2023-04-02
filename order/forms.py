from django import forms

from .models import LaundryItem

class LaundryItemForm(forms.ModelForm):
    class Meta:
        model = LaundryItem
        fields = ('name', 'description', 'price', 'image')