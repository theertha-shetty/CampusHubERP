import json
import os
import csv
import pickle
import re


def save_students(students, filename="students.json"):
    with open(filename, "w") as file:
        json.dump(students, file, indent=4)

    print("Student records saved successfully")


def load_students(filename="students.json"):
    if not os.path.exists(filename):
        print("Student file not found")
        return []

    with open(filename, "r") as file:
        students = json.load(file)

    print("Student records loaded successfully")
    return students


def add_student(students, student_id, name, course):
    student = {
        "student_id": student_id,
        "name": name,
        "course": course
    }

    students.append(student)
    return students


def display_students(students):
    for student in students:
        print(student)
# CSV FILE HANDLING

def save_students_csv(students, filename="students.csv"):
    if not students:
        return

    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=students[0].keys()
        )
        writer.writeheader()
        writer.writerows(students)

    print("Students saved to CSV successfully")


def load_students_csv(filename="students.csv"):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        return list(reader)


# PICKLE SERIALIZATION

def serialize_students(students, filename="students.pkl"):
    with open(filename, "wb") as file:
        pickle.dump(students, file)

    print("Students serialized successfully")


def deserialize_students(filename="students.pkl"):
    with open(filename, "rb") as file:
        students = pickle.load(file)

    print("Students deserialized successfully")
    return students


# REGEX VALIDATION

def validate_email(email):
    pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
    return bool(re.match(pattern, email))


def validate_phone(phone):
    pattern = r"^[0-9]{10}$"
    return bool(re.match(pattern, phone))

def validate_student(student):
    required_fields = ["student_id", "name", "course"]

    for field in required_fields:
        if field not in student or not student[field]:
            return False

    return True


def safe_load_students(filename="students.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print("File not found")
        return []

    except json.JSONDecodeError:
        print("Invalid JSON file")
        return []


def search_student(students, student_id):
    for student in students:
        if str(student["student_id"]) == str(student_id):
            return student

    return None