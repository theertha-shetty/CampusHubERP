from app.entity_routes import entity_api
from flask import Flask, request, jsonify
import sqlite3


def create_app(database="campushub.db"):
    app = Flask(__name__)
    app.register_blueprint(entity_api)
    def get_connection():
        return sqlite3.connect(database)

    @app.route("/", methods=["GET"])
    def home():
        return jsonify({
            "message": "Welcome to CampusHubERP API"
        }), 200

    @app.route("/health", methods=["GET"])
    def health_check():
        return jsonify({
            "status": "healthy",
            "application": "CampusHubERP"
        }), 200
        return jsonify({
            "message": "Welcome to CampusHubERP API"
        }), 200

    @app.route("/students", methods=["GET"])
    def get_students():
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

        connection.close()

        result = [
            {
                "student_id": row[0],
                "name": row[1],
                "course": row[2],
                "email": row[3]
            }
            for row in students
        ]

        return jsonify(result), 200

    @app.route("/students", methods=["POST"])
    def add_student():
        data = request.get_json(silent=True) or {}

        required = ["student_id", "name", "course", "email"]

        if not all(data.get(field) for field in required):
            return jsonify({"error": "All fields are required"}), 400

        connection = get_connection()

        try:
            cursor = connection.cursor()

            cursor.execute("""
                INSERT INTO students
                (student_id, name, course, email)
                VALUES (?, ?, ?, ?)
            """, (
                data["student_id"],
                data["name"],
                data["course"],
                data["email"]
            ))

            connection.commit()

            return jsonify({"message": "Student added"}), 201

        except sqlite3.IntegrityError:
            return jsonify({"error": "Student ID already exists"}), 409

        finally:
            connection.close()

    @app.route("/students/<int:student_id>", methods=["PUT"])
    def update_student(student_id):
        data = request.get_json(silent=True) or {}

        required = ["name", "course", "email"]

        if not all(data.get(field) for field in required):
            return jsonify({"error": "All fields are required"}), 400

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE students
            SET name = ?, course = ?, email = ?
            WHERE student_id = ?
        """, (
            data["name"],
            data["course"],
            data["email"],
            student_id
        ))

        connection.commit()
        updated = cursor.rowcount
        connection.close()

        if updated == 0:
            return jsonify({"error": "Student not found"}), 404

        return jsonify({"message": "Student updated"}), 200

    @app.route("/students/<int:student_id>", methods=["DELETE"])
    def delete_student(student_id):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM students WHERE student_id = ?",
            (student_id,)
        )

        connection.commit()
        deleted = cursor.rowcount
        connection.close()

        if deleted == 0:
            return jsonify({"error": "Student not found"}), 404

        return jsonify({"message": "Student deleted"}), 200

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
