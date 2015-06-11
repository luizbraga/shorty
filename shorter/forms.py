from django import forms

class SubmitForm(forms.Form):
    url = forms.URLField(
        label='URL to be shortened',)