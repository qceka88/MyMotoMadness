import re

from django.core import exceptions


def check_name_symbols_for_non_alphabetical(value):
    if not value.isalpha():
        raise exceptions.ValidationError('Name must be only alphabet symbol!')


def phone_validator(value):
    match = re.match(r"^(0|\+359)(\d{9})\b", value)
    if not match:
        raise exceptions.ValidationError('Valid phone format is 0xxxxxxxxx or +359xxxxxxxxxx!')
