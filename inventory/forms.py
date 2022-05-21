from django import forms
from .models import Warehouse

class CreateInventory(forms.Form):
    product = forms.CharField(label="Product", max_length = 50, required = True)
    warehouse = forms.ModelChoiceField(label='Warehouse', queryset= Warehouse.objects.all(), required = True)
    cost = forms.DecimalField(label = 'Cost', max_digits = 7, decimal_places = 2, required = True)
    quantity = forms.IntegerField(label ='Quantity', required = True, min_value = 1)

class CreateWarehouse(forms.Form):
    city = forms.CharField(label = 'City',max_length = 50, required = True)
    state = forms.CharField(label = 'State', max_length = 50, required = True)
    capacity = forms.IntegerField(label = 'Capacity', required = True, min_value = 1)
