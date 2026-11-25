import re


def validate_email(email):
    return bool(re.match(r"^[\w.-]+@[\w.-]+\.\w+$", email))


def validate_name(name):
    return isinstance(name, str) and len(name.strip()) >= 2


def validate_age(age):
    return isinstance(age, int) and 1 <= age <= 100


def validate_required(value):
    return value is not None and str(value).strip() != ""


def validate_student_id(student_id):
    return bool(re.match(r"^ST\d{3,}$", str(student_id)))


def validate_faculty_id(faculty_id):
    return bool(re.match(r"^F\d{3,}$", str(faculty_id)))


def validate_course_code(course_code):
    return bool(re.match(r"^[A-Z]{2,4}\d{3,}$", str(course_code)))