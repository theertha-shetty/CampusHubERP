
class Student:

    college_name = "CampusHub College"

    def __init__(self, name):
        self.name = name

    # Instance Method
    def display_name(self):
        return self.name

    # Static Method
    @staticmethod
    def is_adult(age):
        return age >= 18

    # Class Method
    @classmethod
    def get_college_name(cls):
        return cls.college_name


student = Student("Theertha")

print("Student Name:", student.display_name())

print("Is Adult:", Student.is_adult(21))

print("College Name:", Student.get_college_name())
