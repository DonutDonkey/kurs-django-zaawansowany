from django import forms

class NaszForm(forms.Form):
    imie = forms.CharField(label='Imie', max_length=20)
    rok = forms.IntegerField()