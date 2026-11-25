from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.db import Base


class StudentDB(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    course = Column(String, nullable=False)
    email = Column(String)


class FacultyDB(Base):
    __tablename__ = "faculty"

    faculty_id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    email = Column(String)
    department = Column(String)


class CourseDB(Base):
    __tablename__ = "courses"

    course_code = Column(String, primary_key=True)
    course_name = Column(String, nullable=False)
    credits = Column(Integer, nullable=False)


class EnrollmentDB(Base):
    __tablename__ = "enrollments"

    student_id = Column(String, primary_key=True)
    course_code = Column(String, primary_key=True)
    enrollment_date = Column(String)
    status = Column(String, default="Active")