from app.database.db import SessionLocal
from app.database.models import (
    StudentDB, FacultyDB, CourseDB, EnrollmentDB
)


class Repository:

    def __init__(self):
        self.db = SessionLocal()

    def add(self, record):
        try:
            self.db.add(record)
            self.db.commit()
            self.db.refresh(record)
            return record
        except Exception:
            self.db.rollback()
            raise

    def get_all(self, model):
        return self.db.query(model).all()

    def get_by_id(self, model, record_id):
        return self.db.get(model, record_id)

    def update(self, record):
        try:
            updated = self.db.merge(record)
            self.db.commit()
            return updated
        except Exception:
            self.db.rollback()
            raise

    def delete(self, record):
        try:
            self.db.delete(record)
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise

    def close(self):
        self.db.close()


class StudentRepository(Repository):
    model = StudentDB


class FacultyRepository(Repository):
    model = FacultyDB


class CourseRepository(Repository):
    model = CourseDB


class EnrollmentRepository(Repository):
    model = EnrollmentDB