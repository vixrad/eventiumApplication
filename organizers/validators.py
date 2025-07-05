from django.core.exceptions import ValidationError

def validate_secret_key(value):
    if len(value) != 4 or not value.isdigit() or len(set(value)) != 4:
        raise ValidationError("Your secret key must have 4 unique digits!")