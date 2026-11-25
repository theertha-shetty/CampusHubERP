# CampusHubERP – Campus Management System

## Overview

CampusHubERP is a Python-based Campus Management System developed to simplify and organize academic operations. It provides structured management of students, faculty, courses, and enrollments using Object-Oriented Programming, database integration, and REST API development.

The project demonstrates advanced Python programming concepts through a modular and maintainable application structure.

## Features

- **Student Management:** Add, view, update, search, and remove student records.
- **Faculty Management:** Manage faculty information and departments.
- **Course Management:** Create and manage courses and course details.
- **Enrollment Management:** Manage student course enrollments.
- **Advanced OOP:** Classes, inheritance, polymorphism, descriptors, and metaclasses.
- **Functional Programming:** Lambda functions, map, filter, reduce, and other functional techniques.
- **Iterators and Generators:** Efficient data iteration and generation.
- **Concurrency:** Threading, multiprocessing, and synchronization.
- **Asynchronous Programming:** Asyncio, tasks, queues, locks, and events.
- **File Handling:** CSV, JSON, and Pickle serialization.
- **Database Integration:** SQLite database operations and backup.
- **REST API:** Flask-based API supporting GET, POST, PUT, and DELETE operations.
- **Testing:** Automated tests using Python's unittest framework.

## Technologies Used

- Python
- Flask
- SQLite
- JSON
- CSV
- Pickle
- Git and GitHub
- VS Code

## Project Structure

```text
CampusHubERP/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── models/
│   ├── services/
│   ├── utils/
│   ├── api.py
│   └── main.py
│
├── data/
├── reports/
├── tests/
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/theertha-shetty/CampusHubERP.git
```

2. Navigate to the project folder:

```bash
cd CampusHubERP
```

3. Install Flask:

```bash
python -m pip install flask
```

4. Run the application:

```bash
python -m app.main
```

5. Open the application API in your browser:

```text
http://127.0.0.1:5000/
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/health` | API health check |
| GET | `/students` | Retrieve all students |
| POST | `/students` | Add a student |
| PUT | `/students/<student_id>` | Update a student |
| DELETE | `/students/<student_id>` | Delete a student |

## Running Tests

Run the API tests:

```bash
python -m tests.test_api
```

Run the complete test suite:

```bash
python -m unittest discover -s tests
```

## Development Roadmap

The project was developed across nine weeks:

1. Advanced Object-Oriented Programming
2. Functional Programming
3. Iterators, Generators, and Context Managers
4. Concurrency and Multiprocessing
5. Asynchronous Programming
6. File Handling and Serialization
7. SQLite Database Integration
8. REST API Development
9. Final Integration and Testing

## Project Repository

GitHub: https://github.com/theertha-shetty/CampusHubERP

## Conclusion

CampusHubERP demonstrates the practical application of advanced Python concepts in developing a modular campus management application. It combines object-oriented design, database operations, concurrency, asynchronous programming, and REST API development in one project.
