from django import forms

from .models import LaundryItem

class LaundryItemForm(forms.ModelForm):
    date=forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = LaundryItem
        fields = '__all__'