from django.core.exceptions import ValidationError

def validate_rok(value):
    if value > 2020:
        raise ValidationError('Rok wiekszy niz 2020')
    return value