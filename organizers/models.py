from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models
from .validators import validate_secret_key


class Organizer(models.Model):
    company_name = models.CharField(
        max_length=110,
        unique=True,
        validators=[
            MinLengthValidator(2),
            RegexValidator(
                regex=r'^[A-Za-z0-9\- ]+$',
                message="The company name is invalid!",
            ),
        ],
        help_text="*Allowed names contain letters, digits, spaces, and hyphens.",
    )

    phone_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\d+$',
                message="Phone number must contain digits only.",
            ),
        ],
        error_messages={
            'unique': "That phone number is already in use!",
        },
    )

    secret_key = models.CharField(
        max_length=4,
        validators=[validate_secret_key],
        help_text="*Pick a combination of 4 unique digits.",
    )

    website = models.URLField(
        blank=True,
        null=True,
    )