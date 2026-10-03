"""Controller layer managing business logic and local in-memory storage."""
from models.student_model import build_student

# In-memory storage for students (ID -> Student mapping)
_students_db: dict[int, dict] = {}
_current_id_counter: int = 1


def reset_data() -> None:
    """Reset the in-memory database and ID counter. Useful for testing."""
    global _students_db, _current_id_counter
    _students_db.clear()
    _current_id_counter = 1


def seed_sample_students() -> list[dict]:
    """Seed the database with at least 5 sample university student records."""
    reset_data()
    sample_students = [
        {
            "name": "Rahul Patel",
            "email": "rahul@example.com",
            "course": "B.Tech Computer Engineering",
            "semester": 5,
        },
        {
            "name": "Priya Sharma",
            "email": "priya.sharma@example.com",
            "course": "B.Tech Information Technology",
            "semester": 3,
        },
        {
            "name": "Amit Kumar",
            "email": "amit.kumar@example.com",
            "course": "B.Tech Electronics & Communication",
            "semester": 7,
        },
        {
            "name": "Ananya Iyer",
            "email": "ananya.iyer@example.com",
            "course": "B.Tech Mechanical Engineering",
            "semester": 1,
        },
        {
            "name": "Rohan Verma",
            "email": "rohan.verma@example.com",
            "course": "B.Tech Computer Engineering",
            "semester": 5,
        },
    ]
    created = []
    for student_data in sample_students:
        created.append(create_student(student_data))
    return created


def create_student(student_data: dict) -> dict:
    """Create a new student record with auto-incremented ID and store in memory."""
    global _current_id_counter
    new_id = _current_id_counter
    _current_id_counter += 1

    student = build_student(student_data, new_id)
    _students_db[new_id] = student
    return student


def get_all_students(
    name: str | None = None,
    course: str | None = None,
    semester: int | None = None,
    skip: int = 0,
    limit: int = 100,
) -> list[dict]:
    """Retrieve all student records with optional search/filter and pagination."""
    students = list(_students_db.values())

    # Filter by name (case-insensitive substring match)
    if name is not None and name.strip():
        students = [s for s in students if name.lower() in s.name.lower()]

    # Filter by course (case-insensitive substring match)
    if course is not None and course.strip():
        students = [s for s in students if course.lower() in s.course.lower()]

    # Filter by semester (exact match)
    if semester is not None:
        students = [s for s in students if s.semester == semester]

    # Apply pagination
    return students[skip : skip + limit]


def get_student_by_id(student_id: int) -> dict | None:
    """Retrieve a single student record by its unique ID."""
    return _students_db.get(student_id)


def update_student(student_id: int, student_data: dict) -> dict | None:
    """Update an existing student record in memory."""
    existing_student = _students_db.get(student_id)
    if existing_student is None:
        return None

    # Get updated values, falling back to existing values if not provided
    updated_dict = dict(existing_student)
    update_data = {key: value for key, value in student_data.items() if value is not None}

    for key, value in update_data.items():
        if value is not None:
            updated_dict[key] = value

    updated_student = build_student(updated_dict)
    _students_db[student_id] = updated_student
    return updated_student


def delete_student(student_id: int) -> bool:
    """Delete a student record by ID. Returns True if deleted, False if not found."""
    if student_id in _students_db:
        del _students_db[student_id]
        return True
    return False
