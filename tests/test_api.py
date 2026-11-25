
import unittest

from app.api import create_app


class TestCampusHubAPI(unittest.TestCase):

    def setUp(self):
        self.app = create_app("campushub.db")
        self.client = self.app.test_client()

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)

    def test_get_students(self):
        response = self.client.get("/students")
        self.assertEqual(response.status_code, 200)

    def test_get_faculty(self):
        response = self.client.get("/faculty")
        self.assertEqual(response.status_code, 200)

    def test_get_courses(self):
        response = self.client.get("/courses")
        self.assertEqual(response.status_code, 200)

    def test_get_enrollments(self):
        response = self.client.get("/enrollments")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
