
import sqlite3
import json
import os

DATABASE = "campushub.db"
DATA_FOLDER = "data"

TABLES = [
    "students",
    "faculty",
    "courses",
    "enrollments"
]


def export_data():
    os.makedirs(DATA_FOLDER, exist_ok=True)

    connection = sqlite3.connect(DATABASE)

    try:
        cursor = connection.cursor()

        for table in TABLES:
            cursor.execute(f"SELECT * FROM {table}")

            columns = [
                description[0]
                for description in cursor.description
            ]

            records = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]

            with open(
                f"{DATA_FOLDER}/{table}.json",
                "w",
                encoding="utf-8"
            ) as file:
                json.dump(records, file, indent=4)

            print(f"{table}.json exported successfully")

    finally:
        connection.close()


def import_data():
    connection = sqlite3.connect(DATABASE)

    try:
        cursor = connection.cursor()

        for table in TABLES:
            file_path = f"{DATA_FOLDER}/{table}.json"

            if not os.path.exists(file_path):
                print(f"{file_path} not found")
                continue

            with open(file_path, "r", encoding="utf-8") as file:
                records = json.load(file)

            for record in records:
                columns = list(record.keys())

                placeholders = ", ".join(["?"] * len(columns))
                column_names = ", ".join(columns)

                values = [record[column] for column in columns]

                query = (
                    f"INSERT OR REPLACE INTO {table} "
                    f"({column_names}) VALUES ({placeholders})"
                )

                cursor.execute(query, values)

            print(f"{table}.json imported successfully")

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


if __name__ == "__main__":
    export_data()
    print("\nAll data exported successfully.")
