from django.core import exceptions


def check_name_symbols_for_non_alphabetical(value):
    if not value.isalpha():
        raise exceptions.ValidationError('Name must be only alphabet symbol!')

