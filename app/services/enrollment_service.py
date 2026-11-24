
from app.models.enrollment import Enrollment
from app.utils.decorators import log_operation


class EnrollmentService:

    def __init__(self):
        self.enrollments = []

    @log_operation
    def enroll_student(self, student_id, course_code):

        enrollment = Enrollment(
            student_id,
            course_code
        )

        self.enrollments.append(enrollment)

        return enrollment

    def get_all_enrollments(self):
        return self.enrollments


    def get_enrollments_by_student(self, student_id):

        return list(
            filter(
                lambda enrollment: enrollment.student_id == student_id,
                self.enrollments
            )
        )
