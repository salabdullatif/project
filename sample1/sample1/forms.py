from django import forms
from django.template.defaultfilters import default
from django.forms.widgets import Widget, RadioSelect
from Tkconstants import RADIOBUTTON
from django.db import models

countries = (('US', 'United States'), ('GB', 'Great Britain'))

class createJobForm(forms.Form):
    file = forms.FileField()
    title = forms.CharField(max_length=100)
    instructions = forms.CharField(widget=forms.Textarea(attrs={'rows':6, 'cols':30})) 
    cml = forms.CharField(widget=forms.Textarea(attrs={'rows':6, 'cols':30})) 
    payment_cents = forms.IntegerField(min_value=5, max_value=100, widget=forms.NumberInput)
    judgments_per_unit = forms.IntegerField(min_value=1, max_value=1000, widget=forms.NumberInput)
    confidence_fields = forms.CharField(required=False) 
    max_judgments_per_unit = forms.IntegerField(min_value=1, max_value=5, widget=forms.NumberInput, required=False)
    min_unit_confidence = forms.DecimalField(required=False)
    auto_order = forms.BooleanField(required=False)
    auto_order_threshold = forms.IntegerField(min_value=1, max_value=99, widget=forms.NumberInput, required=False)
    auto_order_timeout = forms.IntegerField(min_value=1, max_value=99, widget=forms.NumberInput, required=False)
    included_countries = forms.MultipleChoiceField(choices=countries, required=False)
    excluded_countries = forms.MultipleChoiceField(choices=countries, required=False)
    units_per_assignment = forms.IntegerField(min_value=1, max_value=99, widget=forms.NumberInput, required=False)
    
    
    #data / job setting (price/number of worker/quality))