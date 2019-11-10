from django.core.exceptions import ValidationError

def validate_rok(value):
    if value > 2020:
        raise ValidationError("Rok jest wiekszy niz 2020")
    return value