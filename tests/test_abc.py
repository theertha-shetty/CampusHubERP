
from app.core.abc_interfaces import Person


class Student(Person):

    def display_details(self):
        print("Student details displayed")

    def to_dict(self):
        return {"name": "Theertha"}


student = Student()

student.display_details()
print(student.to_dict())

