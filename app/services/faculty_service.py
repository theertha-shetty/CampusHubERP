
from app.models.faculty import Faculty
from app.utils.decorators import log_operation


class FacultyService:

    def __init__(self):
        self.faculties = []

    @log_operation
    def add_faculty(self, faculty_id, name, age, email, department):

        faculty = Faculty(
            faculty_id,
            name,
            age,
            email,
            department
        )

        self.faculties.append(faculty)

        return faculty

    def get_all_faculty(self):
        return self.faculties


    def get_faculty_by_department(self, department):

        return list(
            filter(
                lambda faculty: faculty.department == department,
                self.faculties
            )
        )
