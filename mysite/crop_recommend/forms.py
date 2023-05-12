from django import forms

class condition_input(forms.Form):
    nitrogen = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=True)
    phosphorous = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=True)
    pottasium = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=True)
    temperature = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=True)
    humidity = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=True)
    ph = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=True)
    rainfall = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=True)