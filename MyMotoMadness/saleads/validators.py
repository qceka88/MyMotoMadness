from django.core import exceptions


def check_files_quantity(value: int):
    if not 3 <= value <= 8:
        return exceptions.ValidationError('Pictures should  be between 3 and 8 including!')
