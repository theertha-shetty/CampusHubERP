import json
import csv


def save_json(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def load_json(filename):
    with open(filename, "r") as file:
        return json.load(file)


def save_csv(data, filename):
    if not data:
        return

    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def load_csv(filename):
    with open(filename, "r", newline="") as file:
        return list(csv.DictReader(file))