from django.core.exceptions import ValidationError
import datetime


def validate_past_dates(value):
    if value > datetime.date.today():
        raise ValidationError("The date cannot be in the future!")
    return value
