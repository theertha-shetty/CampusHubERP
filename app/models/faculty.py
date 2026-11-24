
from app.models.person import BasePerson


class Faculty(BasePerson):

    def __init__(self, faculty_id, name, age, email, department):
        super().__init__(name, age, email, department)
        self.faculty_id = faculty_id

    def display_details(self):
        print("Faculty ID:", self.faculty_id)
        super().display_details()

    def to_dict(self):
        data = super().to_dict()
        data["faculty_id"] = self.faculty_id
        return data

