import re


def validate_email(email):
    pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
    return bool(re.match(pattern, email))


def validate_name(name):
    return isinstance(name, str) and len(name.strip()) >= 2


def validate_age(age):
    return isinstance(age, int) and 1 <= age <= 100


def validate_required(value):
    return value is not None and str(value).strip() != ""