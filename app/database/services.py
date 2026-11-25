from app.database.repository import (
    StudentRepository,
    FacultyRepository,
    CourseRepository,
    EnrollmentRepository
)


class BaseService:

    def __init__(self, repository):
        self.repository = repository

    def get_all(self):
        return self.repository.get_all(self.repository.model)

    def get_by_id(self, record_id):
        return self.repository.get_by_id(
            self.repository.model, record_id
        )

    def add(self, record):
        return self.repository.add(record)

    def update(self, record):
        return self.repository.update(record)

    def delete(self, record):
        self.repository.delete(record)

    def close(self):
        self.repository.close()


class StudentServiceDB(BaseService):
    def __init__(self):
        super().__init__(StudentRepository())


class FacultyServiceDB(BaseService):
    def __init__(self):
        super().__init__(FacultyRepository())


class CourseServiceDB(BaseService):
    def __init__(self):
        super().__init__(CourseRepository())


class EnrollmentServiceDB(BaseService):
    def __init__(self):
        super().__init__(EnrollmentRepository())