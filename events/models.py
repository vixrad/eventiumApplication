from django.utils import timezone
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from organizers.models import Organizer


class Event(models.Model):
    slogan = models.CharField(
        max_length=120,
        validators=[
            MinLengthValidator(2),
        ]
    )

    location = models.CharField(
        max_length=120,
        validators=[
            MinLengthValidator(2),
        ]
    )

    start_time = models.DateTimeField(
        default=timezone.now,
    )

    available_tickets = models.IntegerField(
        validators=[
            MinValueValidator(0),
        ]
    )

    key_features = models.TextField(
        blank=True,
        null=True,
    )

    banner_url = models.URLField(
        blank=True,
        null=True,
    )

    organizer = models.ForeignKey(
        Organizer,
        on_delete=models.CASCADE,
        editable=False,
        related_name='events',
    )