
from flask import Blueprint, request, jsonify

from app.database.services import (
    FacultyServiceDB,
    CourseServiceDB,
    EnrollmentServiceDB
)

from app.database.models import (
    FacultyDB,
    CourseDB,
    EnrollmentDB
)

entity_api = Blueprint("entity_api", __name__)


def register_crud(path, service_class, model, id_field):

    @entity_api.route(
        path, methods=["GET"], endpoint=id_field + "_get_all"
    )
    def get_all():
        service = service_class()
        try:
            records = service.get_all()
            return jsonify([
                {
                    column.name: getattr(record, column.name)
                    for column in model.__table__.columns
                }
                for record in records
            ]), 200
        finally:
            service.close()

    @entity_api.route(
        path, methods=["POST"], endpoint=id_field + "_create"
    )
    def create():
        data = request.get_json(silent=True) or {}
        service = service_class()
        try:
            if id_field not in data:
                return jsonify({"error": f"{id_field} required"}), 400

            service.add(model(**data))
            return jsonify({"message": "Record added"}), 201
        except Exception:
            return jsonify({"error": "Unable to add record"}), 400
        finally:
            service.close()

    @entity_api.route(
        path + "/<string:record_id>",
        methods=["PUT"], endpoint=id_field + "_update"
    )
    def update(record_id):
        data = request.get_json(silent=True) or {}
        service = service_class()
        try:
            record = service.get_by_id(record_id)

            if not record:
                return jsonify({"error": "Record not found"}), 404

            for key, value in data.items():
                if key != id_field and hasattr(record, key):
                    setattr(record, key, value)

            service.update(record)
            return jsonify({"message": "Record updated"}), 200
        finally:
            service.close()

    @entity_api.route(
        path + "/<string:record_id>",
        methods=["DELETE"], endpoint=id_field + "_delete"
    )
    def delete(record_id):
        service = service_class()
        try:
            record = service.get_by_id(record_id)

            if not record:
                return jsonify({"error": "Record not found"}), 404

            service.delete(record)
            return jsonify({"message": "Record deleted"}), 200
        finally:
            service.close()


register_crud("/faculty", FacultyServiceDB, FacultyDB, "faculty_id")
register_crud("/courses", CourseServiceDB, CourseDB, "course_code")


# Enrollment APIs (composite primary key)

@entity_api.route("/enrollments", methods=["GET"])
def get_enrollments():
    service = EnrollmentServiceDB()
    try:
        records = service.get_all()
        return jsonify([
            {
                "student_id": r.student_id,
                "course_code": r.course_code,
                "enrollment_date": r.enrollment_date,
                "status": r.status
            }
            for r in records
        ]), 200
    finally:
        service.close()


@entity_api.route("/enrollments", methods=["POST"])
def add_enrollment():
    data = request.get_json(silent=True) or {}

    if not data.get("student_id") or not data.get("course_code"):
        return jsonify({
            "error": "student_id and course_code required"
        }), 400

    service = EnrollmentServiceDB()
    try:
        service.add(EnrollmentDB(**data))
        return jsonify({"message": "Enrollment added"}), 201
    except Exception:
        return jsonify({"error": "Unable to add enrollment"}), 400
    finally:
        service.close()


@entity_api.route(
    "/enrollments/<string:student_id>/<string:course_code>",
    methods=["PUT"]
)
def update_enrollment(student_id, course_code):
    data = request.get_json(silent=True) or {}
    service = EnrollmentServiceDB()

    try:
        record = service.repository.db.get(
            EnrollmentDB, (student_id, course_code)
        )

        if not record:
            return jsonify({"error": "Enrollment not found"}), 404

        for key, value in data.items():
            if key not in ("student_id", "course_code") and hasattr(record, key):
                setattr(record, key, value)

        service.update(record)
        return jsonify({"message": "Enrollment updated"}), 200
    finally:
        service.close()


@entity_api.route(
    "/enrollments/<string:student_id>/<string:course_code>",
    methods=["DELETE"]
)
def delete_enrollment(student_id, course_code):
    service = EnrollmentServiceDB()

    try:
        record = service.repository.db.get(
            EnrollmentDB, (student_id, course_code)
        )

        if not record:
            return jsonify({"error": "Enrollment not found"}), 404

        service.delete(record)
        return jsonify({"message": "Enrollment deleted"}), 200
    finally:
        service.close()
