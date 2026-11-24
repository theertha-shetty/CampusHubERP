
from datetime import datetime


class Enrollment:

    def __init__(self, student_id, course_code):
        self.student_id = student_id
        self.course_code = course_code
        self.enrollment_date = datetime.now()
        self.status = "Active"

    def display_details(self):
        print("Student ID:", self.student_id)
        print("Course Code:", self.course_code)
        print("Enrollment Date:", self.enrollment_date)
        print("Status:", self.status)

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "course_code": self.course_code,
            "enrollment_date": self.enrollment_date.isoformat(),
            "status": self.status
        }

