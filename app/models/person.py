
from app.core.abc_interfaces import Person
from app.core.descriptors import (
    NameDescriptor,
    EmailDescriptor,
    AgeDescriptor
)
from app.core.metaclasses import ModelMeta


class BasePerson(Person, metaclass=ModelMeta):

    name = NameDescriptor()
    email = EmailDescriptor()
    age = AgeDescriptor()

    def __init__(self, name, age, email, department):
        self.name = name
        self.age = age
        self.email = email
        self.department = department

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Email:", self.email)
        print("Department:", self.department)

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "department": self.department
        }

