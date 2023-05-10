from django import forms

class crop_input(forms.Form):
    nitrogen = forms.CharField(widget=forms.TextInput, required=True)
    phosphorous = forms.CharField(widget=forms.TextInput, required=True)
    pottasium = forms.CharField(widget=forms.TextInput, required=True)
    ph = forms.CharField(widget=forms.TextInput, required=True)
    rainfall = forms.CharField(widget=forms.TextInput, required=True)
