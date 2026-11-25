
from multiprocessing import connection
import tempfile
import os
import sqlite3
import unittest

from app.api import create_app


class TestCampusHubAPI(unittest.TestCase):

    def setUp(self):
        temp = tempfile.NamedTemporaryFile(delete=False)
        self.database = temp.name
        temp.close()

        connection = sqlite3.connect(self.database)

        connection.execute("""
    CREATE TABLE students (
        student_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        course TEXT NOT NULL,
        email TEXT
    )
""")

        connection.commit()
        connection.close()

        self.app = create_app(self.database)
        self.client = self.app.test_client()

    def tearDown(self):
        if os.path.exists(self.database):
            os.remove(self.database)

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_add_student(self):
        response = self.client.post("/students", json={
            "student_id": 101,
            "name": "Ananya",
            "course": "Computer Science",
            "email": "ananya@gmail.com"
        })
        self.assertEqual(response.status_code, 201)

    def test_get_students(self):
        self.client.post("/students", json={
            "student_id": 101,
            "name": "Ananya",
            "course": "Computer Science",
            "email": "ananya@gmail.com"
        })

        response = self.client.get("/students")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)

    def test_update_student(self):
        self.client.post("/students", json={
            "student_id": 101,
            "name": "Ananya",
            "course": "Computer Science",
            "email": "ananya@gmail.com"
        })

        response = self.client.put("/students/101", json={
            "name": "Ananya Shetty",
            "course": "Data Science",
            "email": "ananya@gmail.com"
        })
        self.assertEqual(response.status_code, 200)

    def test_delete_student(self):
        self.client.post("/students", json={
            "student_id": 101,
            "name": "Ananya",
            "course": "Computer Science",
            "email": "ananya@gmail.com"
        })

        response = self.client.delete("/students/101")
        self.assertEqual(response.status_code, 200)

    def test_add_student_missing_fields(self):
        response = self.client.post("/students", json={
            "student_id": 102,
            "name": "Rahul"
        })
        self.assertEqual(response.status_code, 400)

    def test_duplicate_student(self):
        student = {
            "student_id": 101,
            "name": "Ananya",
            "course": "Computer Science",
            "email": "ananya@gmail.com"
        }

        self.client.post("/students", json=student)
        response = self.client.post("/students", json=student)

        self.assertEqual(response.status_code, 409)

    def test_update_missing_student(self):
        response = self.client.put("/students/999", json={
            "name": "Rahul",
            "course": "Python",
            "email": "rahul@gmail.com"
        })
        self.assertEqual(response.status_code, 404)

    def test_delete_missing_student(self):
        response = self.client.delete("/students/999")
        self.assertEqual(response.status_code, 404)
        
if __name__ == "__main__":
    unittest.main()
