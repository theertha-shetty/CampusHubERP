
import json
import csv
import os


def save_json(data, filename):
    os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def save_csv(data, filename):
    if not data:
        return

    os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def load_csv(filename):
    with open(filename, "r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


# Student JSON functions
def save_student_json(data):
    save_json(data, "data/students.json")


def load_student_json():
    return load_json("data/students.json")


# Course JSON functions
def save_courses_json(data):
    save_json(data, "data/courses.json")


def load_courses_json():
    return load_json("data/courses.json")


# Faculty JSON functions
def save_faculty_json(data):
    save_json(data, "data/faculty.json")


def load_faculty_json():
    return load_json("data/faculty.json")


# Enrollment JSON functions
def save_enrollments_json(data):
    save_json(data, "data/enrollments.json")


def load_enrollments_json():
    return load_json("data/enrollments.json")
