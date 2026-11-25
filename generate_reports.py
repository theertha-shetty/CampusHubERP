import sqlite3
import json
import os

os.makedirs("reports", exist_ok=True)

connection = sqlite3.connect("campushub.db")
cursor = connection.cursor()

report_files = {
    "students": "student_report.json",
    "faculty": "faculty_report.json",
    "courses": "course_report.json"
}

for table, filename in report_files.items():
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    columns = [item[0] for item in cursor.description]

    data = [dict(zip(columns, row)) for row in rows]

    with open(os.path.join("reports", filename), "w") as file:
        json.dump(data, file, indent=4)

    print(filename, "generated:", len(data), "records")

connection.close()