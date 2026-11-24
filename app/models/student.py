
from app.models.person import BasePerson


class Student(BasePerson):

    def __init__(self, student_id, name, age, email, department):
        super().__init__(name, age, email, department)
        self.student_id = student_id

    def display_details(self):
        print("Student ID:", self.student_id)
        super().display_details()

    def to_dict(self):
        data = super().to_dict()
        data["student_id"] = self.student_id
        return data
        
    def __str__(self):
        return f"Student: {self.name} ({self.student_id})"

    def __repr__(self):
        return f"Student(student_id={self.student_id}, name={self.name})"