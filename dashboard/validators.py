import re

from django.core.exceptions import ValidationError


class NumberValidator(object):
    def validate(self, password, user=None):
        if not re.findall('\d', password):
            raise ValidationError(
                ("Su contraseña debe de tener al menos un digito, 0-9."),
                code='password_no_number',
            )

    def get_help_text(self):
        return (
            "Su contraseña debe de tener al menos un digito, 0-9."
        )


class UppercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError(
                ("Su contreseña debe de tener almenos una letra Mayuscula, A-Z."),
                code='password_no_upper',
            )

    def get_help_text(self):
        return (
            "Su contreseña debe de tener almenos una letra Mayuscula, A-Z."
        )


class LowercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[a-z]', password):
            raise ValidationError(
                ("Su contreseña debe de tener almenos una letra Minuscula, a-z."),
                code='password_no_lower',
            )

    def get_help_text(self):
        return (
            "Su contreseña debe de tener almenos una letra Minuscula, a-z."
        )


class SymbolValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
            raise ValidationError(
                ("Su contreseña debe de tener almenos un symbolo: " +
                  "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"),
                code='password_no_symbol',
            )

    def get_help_text(self):
        return (
            "Su contreseña debe de tener almenos un symbolo: " +
            "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"
        )