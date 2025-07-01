from django import forms
from .models import CoffeeVariety
    
class CoffeeStoreForm(forms.Form):
    coffee_variety = forms.ModelChoiceField(
        queryset=CoffeeVariety.objects.all(),
        label="Select Coffee Variety",
        empty_label="Choose...",
    )