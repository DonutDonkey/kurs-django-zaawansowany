from django import forms
from django.core.validators import MaxValueValidator
from .validators import validate_rok

class NaszForm(forms.Form):
    imie = forms.CharField(label="Imie", max_length=20)
    rok = forms.IntegerField(validators=[validate_rok])

    # def clean_rok(self):
    #     rok = self.cleaned_data.get('rok')
    #     if rok > 2020:
    #         raise forms.ValidationError("Rok jest wiekszy niz 2020")
    #     return rok

    # def clean(self):
    #     cleaned_data = super(NaszForm, self).clean()
    #     return validate_rok(cleaned_data.get('rok'))