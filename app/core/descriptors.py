
class NameDescriptor:
    def __get__(self, instance, owner):
        return instance._name

    def __set__(self, instance, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty")

        instance._name = value


class EmailDescriptor:
    def __get__(self, instance, owner):
        return instance._email

    def __set__(self, instance, value):
        if "@" not in value:
            raise ValueError("Invalid email address")

        instance._email = value


class AgeDescriptor:
    def __get__(self, instance, owner):
        return instance._age

    def __set__(self, instance, value):
        if not 16 <= value <= 80:
            raise ValueError("Age must be between 16 and 80")

        instance._age = value
