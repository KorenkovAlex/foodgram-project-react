from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


def validate_username(username: str):
    if username == 'me':
        raise ValidationError('Нельзя использователь имя пользователя "me" ')
    regex_validator = RegexValidator(
        regex=r'^[\w.@+-]+\Z',
        message='Только буквы, цифры и @/./+/-/_')
    regex_validator(username)
