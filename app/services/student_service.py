
from app.models.student import Student
from app.utils.decorators import log_operation


class StudentService:

    def __init__(self):
        self.students = []

    @log_operation
    def add_student(self, student_id, name, age, email, department):

        student = Student(
            student_id,
            name,
            age,
            email,
            department
        )

        self.students.append(student)

        return student

    def get_all_students(self):

        return self.students

    def get_students_by_department(self, department):

        return list(
            filter(
                lambda student: student.department == department,
                self.students
            )
        )

    def remove_student(self, student_id):

        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return True

        return False

    def update_student(self, student_id, name, age, email, department):

        for student in self.students:
            if student.student_id == student_id:

                student.name = name
                student.age = age
                student.email = email
                student.department = department

                return True

        return False

    def list_students(self):

        sorted_students = sorted(
            self.students,
            key=lambda student: student.name
        )

        student_names = list(
            map(
                lambda student: student.name.upper(),
                sorted_students
            )
        )

        return student_names



    @staticmethod
    def is_eligible_for_admission(age):

        return age >= 16


    @classmethod
    def get_service_name(cls):
        return cls.service_name
    
    service_name = "Student Management Service"






