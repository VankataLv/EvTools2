from django.core.validators import MinLengthValidator, RegexValidator

name_validator = RegexValidator(
    # Cyrillic, Greek & other letters can be added later to the regex pattern above
    regex=r"^[A-Z][a-z'’-]{1,49}$",
    message='First name must start with a capital letter and contain only lowercase letters, apostrophes, or hyphens. '
            'Length must be between 2 to 50 characters.',
)

nickname_validator = RegexValidator(
    regex=r'^[A-Za-z0-9_-]{3,30}$',
    message='Nickname must be between 3 and 30 characters long and can include letters, '
            'numbers, underscores, and hyphens.',
)

phone_number_validator = RegexValidator(
    regex=r'^\+?(\d+){9,}$',
    message='Phone number must be between 9 and 12 digits long, can start with +, no spaces, slashes and dashes.',
)

e_mail_validator = RegexValidator(
    regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
    message='Invalid email address.',
)
