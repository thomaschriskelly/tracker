from django import forms

class ProductForm(forms.Form):
    description = forms.CharField(max_length=32)

class LocationForm(forms.Form):
    datetime = forms.DateTimeField(label='Datetime (eg: 2016-10-13 14:30:59):')
    longitude = forms.CharField(max_length=32)
    latitude = forms.CharField(max_length=32)
    elevation = forms.CharField(max_length=32)
